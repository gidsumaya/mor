from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from device.models import Rainfall
from django.views.generic import TemplateView, ListView
from .models import Mobile, Sms
import csv
import io
from django.contrib import messages
import boto3

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def mobile_upload(request):

    template = "advisory.html"
    data = Mobile.objects.all()

    prompt = {
        'order': 'Order of the CSV should be mobile_owner, mobile_number',
        'mobile': data
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a .csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Mobile.objects.update_or_create(
            mobile_owner=column[0],
            mobile_number=column[1],
        )
    context = {}
    messages.info(request, 'Mobile Numbers uploaded successfully!')
    return render(request, template, context)


def send_sms(request):
    # AWS Credentials
    aws_access_key_id = "AKIAW5FH4YQUGWWOIYMN"
    aws_secret_access_key = "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"
    aws_region_name = "us-east-1"

    z = Rainfall.objects.latest('timestamp', 'level')
    sender_id = "Test"
    sms_message = f'As of {z.timestamp}, the Rainfall Warning is now at {z.level}. Please prepare for evacuation'

    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name
    )

    # Create the topic if it doesn't exist (this is idempotent)
    topic = client.create_topic(Name="notifications")
    topic_arn = topic['TopicArn']  # get its Amazon Resource Name

    # Add SMS Subscribers

    numbers = Mobile.objects.all()
    for i in numbers:
        client.subscribe(
            TopicArn=topic_arn,
            Protocol='sms',
            Endpoint=i.mobile_number
        )

    # Publish a message.
    response = client.publish(
        Message=sms_message,
        TopicArn=topic_arn,
        MessageAttributes={
            'string': {
                'DataType': 'String',
                'StringValue': 'String',
            },
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id
            }
        }
    )

    messages.info(request, 'SMS sent successfully!')
    return HttpResponseRedirect('/advisory/')


def reports(request):
    return HttpResponse('Reports')


class MobileView(TemplateView):
    template_name = 'advisory.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adv"] = Mobile.objects.all()
        return context


class ResView(ListView):
    model = Rainfall
    template_name = 'home.html'
    context_object_name = 'res'
    paginate_by = 8
    queryset = Rainfall.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Rainfall.objects.all()
        return context