from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .utils import analyze_resume
from .form import Resumeform
from .models import Resume,ResumeAnalysis
# Create your views here.


@login_required
def upload_Resume(request):

    resume = Resume.objects.filter(user = request.user).first()
    if resume:
        return redirect('resume-home')

    
    if request.method == 'POST':
            form = Resumeform(request.POST,request.FILES)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.user = request.user
                resume.save()
                return redirect('resume-home')

    else:
        form = Resumeform()

    return render(request,'resume/upload_resume.html',{'form':form})



@login_required
def resume_home(request):

     resume = Resume.objects.filter(user = request.user).first()
     if resume:
          return render(request,'resume/resume_home.html',{'resume':resume})

     else:
          return redirect('resume-upload')


@login_required
def replace_resume(request):

    resume = Resume.objects.filter(user = request.user).first()

    if request.method == 'POST':
         form = Resumeform(request.POST,request.FILES,instance=resume)
         if form.is_valid():
              form.save()
              return redirect('resume-home')

    else:
         form = Resumeform(instance=resume)
    return render(request,'resume/upload_resume.html',{'form':form})


@login_required
def delete_resume(request):

    resume = Resume.objects.filter(
        user=request.user
    ).first()

    if resume:
        resume.resume.delete(save=False)
        resume.delete()

    return redirect('resume-upload')


def  resume_analysis(request):

     resume = Resume.objects.filter(user = request.user).first()

     if not resume:
          return redirect('resume-upload')

     analysis = analyze_resume(resume.resume)

     ResumeAnalysis.objects.update_or_create(
          resume = resume,

          defaults={
               "extracted_text":analysis["text"],
               "sections": ",".join(analysis["sections"]),
               "skills":",".join(analysis["skills"]),
               "score":analysis["score"],
               "suggestions": ','.join(analysis["suggestions"])
          }
     )

     return redirect('analysis-result')


@login_required
def analysis_result(request):

    resume = Resume.objects.filter(
        user=request.user
    ).first()

    if not resume:
        return redirect('resume-upload')

    analysis = ResumeAnalysis.objects.filter(
        resume=resume
    ).first()

    if not analysis:
        return redirect('resume-analysis')

    skills = [
        skill.strip()
        for skill in analysis.skills.split(',')
        if skill.strip()
    ]

    sections = [
        section.strip()
        for section in analysis.sections.split(',')
        if section.strip()
    ]

    suggestions = [
        suggestion.strip()
        for suggestion in analysis.suggestions.split(',')
        if suggestion.strip()
    ]

    context = {
        'analysis': analysis,
        'skills': skills,
        'sections': sections,
        'suggestions': suggestions,
    }

    return render(
        request,
        'resume/resume_analysis.html',
        context
    )
