from django.db import models


class Rainfall(models.Model):
    level = models.CharField(max_length=10, blank=True, default='')
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def update_level(self):
        if 0.1 <= self.amount < 2.5:
            return 'Light'
        elif 2.5 <= self.amount < 7.5:
            return 'Moderate'
        elif 7.5 < self.amount < 15:
            return 'Heavy'
        elif 15 <= self.amount < 30:
            return 'Intense'
        elif 30 <= self.amount < 50:
            return 'Torrential'

    def save(self, *args, **kwargs):
        if not self.level:
            self.level = self.update_level()
        super().save(*args, **kwargs)