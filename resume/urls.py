from django.urls import path
from .import views


urlpatterns = [
    path('resume-upload/',views.upload_Resume,name = 'resume-upload'),
    path('resume-home/',views.resume_home,name='resume-home'),
    path('replace-resume/',views.replace_resume,name='resume-replace'),
    path('delete-resume/',views.delete_resume,name='resume-delete'),
    path('analyze-resume/',views.resume_analysis,name='resume-analyze'),
    path('analysis-result/',views.analysis_result,name='analysis-result')
]

