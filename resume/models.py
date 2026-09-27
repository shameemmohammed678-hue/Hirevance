from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Create your models here.

class Resume(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    resume = models.FileField(
        upload_to='resume/',
        storage=RawMediaCloudinaryStorage()
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(
        Resume,
        on_delete=models.CASCADE
    )

    extracted_text = models.TextField(
        blank=True
    )

    score = models.IntegerField(
        default=0
    )

    skills = models.TextField(
        blank=True
    )

    sections = models.TextField(
        blank=True
    )

    suggestions = models.TextField(
        blank=True
    )

    analyzed_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.resume.user.username} - Resume Analysis"
    