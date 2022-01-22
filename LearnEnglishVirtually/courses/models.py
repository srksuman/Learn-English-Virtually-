from django.db import models

# Create your models here.

class MainContent(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    sub_topic = models.CharField(max_length=200)