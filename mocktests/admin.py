from django.contrib import admin
from .models import MockTest,TestQuestion,TestAttempt,TestAnswer
# Register your models here.


admin.site.register(MockTest)
admin.site.register(TestQuestion)
admin.site.register(TestAttempt)
admin.site.register(TestAnswer)

