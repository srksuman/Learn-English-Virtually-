from django.db import models
from django import forms
# Create your models here.


class MainContent(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    def __str__(self):
        return str(self.topic)
    

class SubContent(models.Model):
    topic = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return str(self.topic.topic)

    def __unicode__(self):
        return str(self.topic.topic)



