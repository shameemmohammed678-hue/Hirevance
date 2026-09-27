from django.contrib import admin
from .models import Category,Question,QuestionOption,Bookmark
# Register your models here.

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(Bookmark)