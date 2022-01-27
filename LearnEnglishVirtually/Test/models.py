from django.db import models
from courses.models import MainContent
# Create your models here.s

class TestManagement(models.Model):
    topic = models.ForeignKey(MainContent,on_delete=models.CASCADE)
    number_of_question = models.IntegerField()
    time = models.FloatField(help_text="Duration of the test in minutes")
    pass_marks = models.FloatField(help_text="Passmarks for test")

    def __str__(self):
        return self.topic

    def get_questions(self):
        pass

    
class Questions(models.Model):
    text = models.CharField(max_length=200)
    test = models.ForeignKey(TestManagement,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

    def get_answers(self):
        pass
    