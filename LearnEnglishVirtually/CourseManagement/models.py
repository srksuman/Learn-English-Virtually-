from django.db import models
from django import forms
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
# Create your models here.
class MainContent(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=200)
    content = RichTextField(null=True,blank=True)
    estimated_time = models.FloatField(null=True,blank=True,default=1)
    sub_topic = models.CharField(max_length=200,null=True,blank=True)
    slug = AutoSlugField(populate_from='topic',unique=True,null=True,blank=True,default=None)

    class Meta:
        verbose_name_plural = 'Course Contents'

    def __str__(self):
        return str(self.topic)

    
    

class EnglishDictionary(models.Model):
    word = models.CharField(max_length= 300)
    class Meta:
        verbose_name_plural = 'English Dictionary'

class EnglishFacts(models.Model):
    fact = RichTextField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'English Facts'

# class SubContent(models.Model):
#     topic = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    # sub_topic = models.CharField(max_length=200)
    # content = RichTextField()

#     def __str__(self):
#         return str(self.topic.topic)

#     def __unicode__(self):
#         return str(self.topic.topic)



