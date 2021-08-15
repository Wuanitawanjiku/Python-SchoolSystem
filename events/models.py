from django.db import models

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=12)
    event_date=models.DateField(null=True)
    event_location=models.CharField(max_length=10)