from django.db import models

# Create your models here.


class MainContent(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    

class SubContent(models.Model):
    topic = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=200)
    content = models.TextField()
