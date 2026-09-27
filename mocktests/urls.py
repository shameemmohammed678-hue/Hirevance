from django.urls import path
from . import views

urlpatterns=[
    path('mock-test-list/', views.Mock_tests,name='mock-test'),
    path('start-test/<int:test_id>/',views.start_test,name='start-test'),
    path('take-test/<int:attempt_id>/',views.take_test,name='take-test'),
    path('submit-answer/<int:attempt_id>/',views.submit_test,name='submit-test'),
    path('test-result/<int:attempt_id>/',views.test_result,name='test-result'),
    path('review-answers/<int:attempt_id>/',views.review_answers,name='review-answer')
]