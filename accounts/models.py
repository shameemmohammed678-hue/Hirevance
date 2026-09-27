from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    skills = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
    college = models.CharField(max_length=200)
    graduation_year = models.IntegerField()



    def __str__(self):
        return self.user.username