from django.db import models
from questions.models import Question,QuestionOption

from django.contrib.auth.models import User
# Create your models here.

class MockTest(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    duration = models.IntegerField()
    difficulty = models.CharField(max_length=50,choices=[('Easy','Easy'),
                                                         ('Medium','Medium'),
                                                         ('Hard','Hard')])

    icon = models.ImageField(
        upload_to='mocktest_icons/',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.title


class TestQuestion(models.Model):
    mock_test = models.ForeignKey(MockTest,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    order = models.IntegerField()


    def __str__(self):
        return  self.mock_test.title


class TestAttempt(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mock_test = models.ForeignKey(MockTest,on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True,null=True)
    score = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.user.username

class TestAnswer(models.Model):
    attempt = models.ForeignKey(TestAttempt,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOption,on_delete=models.CASCADE)


    def __str__(self):
        return self.question.question_text