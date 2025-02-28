from django.db import models

class Data(models.Model):
    socialtime = models.CharField(max_length=100)
    sleeptime = models.CharField(max_length=100)

    def __str__(self):
        return f"Social Time: {self.socialtime} | Sleep Time: {self.sleeptime}"

