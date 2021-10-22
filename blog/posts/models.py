from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000000)
    date_created = models.DateTimeField(default=datetime.datetime.now, blank=True)
