from django.urls import path
from .import views

urlpatterns = [
    path('AI-assistant/',views.AI_assistant,name='AI-assistant'),
    path('ask/',views.ask_ai,name='ask-ai')
]