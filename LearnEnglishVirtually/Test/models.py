from django.db import models
from courses.models import MainContent
from django.contrib.auth.models import User
# Create your models here.s

class TestManagement(models.Model):
    topic = models.ForeignKey(MainContent,on_delete=models.CASCADE)
    number_of_question = models.IntegerField()
    time = models.FloatField(help_text="Duration of the test in minutes")
    pass_marks = models.FloatField(help_text="Passmarks for test")

    def __str__(self):
        return self.topic

    def get_questions(self):
        return questions_set.all()

    class Meta:
        verbose_name_plural ="Test Management"

    
class Questions(models.Model):
    text = models.CharField(max_length=200)
    test = models.ForeignKey(TestManagement,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answers_set.all()

    class Meta:
        verbose_name_plural ="Test Questions"

class Answers(models.Model):
    text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False,null=True)
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question:{self.questions.text} answer: {self.text} correct: {self.correct}"
    
    class Meta:
        verbose_name_plural ="Test Answers"

class Results(models.Model):
    test = models.ForeignKey(TestManagement,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return self.pk

    class Meta:
        verbose_name_plural ="Test Results"
    