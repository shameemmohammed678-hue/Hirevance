from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    question_text = models.TextField()
    difficulty = models.CharField(max_length=50,choices=[('Easy','Easy'),
                                                        ('Medium','Medium'),
                                                        ('Hard','Hard')])
    explanation = models.TextField()

    def __str__(self):
        return self.question_text
    
class QuestionOption(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option_text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.option_text


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    