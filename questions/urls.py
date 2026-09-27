from django.urls import path
from .import views


urlpatterns =[
    path('questions-list/',views.questions_list,name='questions-list'),
    path('question-detail/<int:question_id>/',views.question_detail,name='question-detail'),
    path('question-bookmark/<int:question_id>/',views.bookmark_questions,name='question-bookmark'),
    path('bookmarks/',views.bookmarks,name='bookmarks')
]


