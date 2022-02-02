from django.db import models
import random
from django.contrib.auth.models import User
from CourseManagement.models import MainContent
# Create your models here.


class TestManagement(models.Model):
    topic = models.ForeignKey(MainContent,on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the TestManagement in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %", default=50)

    def __str__(self):
        return f"{self.topic.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Test Management'

class Question(models.Model):
    text = models.CharField(max_length=200)
    TestManagement = models.ForeignKey(TestManagement, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Result(models.Model):
    TestMgmt = models.ForeignKey(TestManagement,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()
    

    def __str__(self):
        return f"Topic: {self.TestMgmt.topic.topic} \t Answer:- {self.user.username} \t Score:- {self.score}"
    
