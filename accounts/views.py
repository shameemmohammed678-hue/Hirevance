from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm,StudentProfileForm
from .models import StudentProfile
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages

from mocktests.models import TestAttempt,TestAnswer
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request,'Registered Successfully')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'accounts/Register.html',{'form':form})
    


def Login(request):

    if request.method == 'POST':
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)

            return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request,'accounts/Login.html',{'form':form})



@login_required
def dashboard(request):

    user = request.user

    completed_test = TestAttempt.objects.filter(user=user,ended_at__isnull = False)

    no_of_complete = completed_test.count()

    average_score = completed_test.aggregate(
        average = Avg('score')
    )['average'] or 0

    question_practiced = TestAnswer.objects.filter(attempt__user = user).count()


    today = timezone.localdate()

    start_of_week = today-timedelta(days=today.weekday())

    weekly_activity = []

    for i in range(7):
        current_day = start_of_week+timedelta(days=i)

        Count = completed_test.filter(ended_at__date = current_day).count()

        weekly_activity.append(Count)


    monthly_activity = []

    start_of_month = today.replace(day=1)

    if today.month == 12:
        next_month = today.replace(
            year=today.year + 1,
            month=1,
            day=1
        )
    else:
        next_month = today.replace(
            month=today.month + 1,
            day=1
        )

    days_in_month = (next_month - start_of_month).days

    for i in range(days_in_month):
        current_day = start_of_month + timedelta(days=i)

        Count = completed_test.filter(
            ended_at__date=current_day
        ).count()

        monthly_activity.append(Count)


    recent_attempts = completed_test.order_by('-ended_at')[:4]



    profile = StudentProfile.objects.filter(user=user).first()


    context = {
        'tests_completed':no_of_complete,
        'average_score':round(average_score),
        'Questions_practised':question_practiced,
        'weekly_activity':weekly_activity,
        'monthly_activity': monthly_activity,
        'recent_attempts':recent_attempts,
        'profile':profile
    }

    return render(request,'accounts/dashboard.html',context)


def change_profile(request):

    profile = StudentProfile.objects.filter(user = request.user).first()
    if request.method == 'POST':
        if profile:
            form = StudentProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request,'Profile Updated Sucessfully !')
                return redirect('change_profile')
            else:
                messages.error(request,'Invalid Details')
        else:
            form = StudentProfileForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, 'Profile Created Successfully!')
                return redirect('change_profile')

            else:

                messages.error(request,'Invalid Details')            
    form = StudentProfileForm(instance=profile)
    return render(request,'accounts/profile.html',{'form':form})


@login_required
def settings_page(request):
    return render(
        request,
        'accounts/settings.html',
        {'user': request.user}
    )


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():
            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                'Password changed successfully!'
            )

            return redirect('settings')

    else:
        form = PasswordChangeForm(request.user)

    return render(
        request,
        'accounts/change_password.html',
        {'form': form}
    )


@login_required
def Logout(request):
    logout(request)
    return redirect('home')