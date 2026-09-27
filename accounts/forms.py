from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import StudentProfile



class RegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True,
    widget = forms.EmailInput(attrs={
        'placeholder':'Enter your email',
        'autocomplete':'email'
    })
    )
    password1 = forms.CharField(required=True,
    widget = forms.PasswordInput(attrs={
        'placeholder':'Enter your Password',
        'autocomplete':'new-password'
    })
    )

    password2 = forms.CharField(required=True,
        widget = forms.PasswordInput(attrs={
            'placeholder':'Confirm your Password',
            'autocomplete':'new-password'
        })
        )


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username':forms.TextInput(attrs={
                'placeholder':'Enter your username',
                'autocomplete':'username'
            }),
        }

class LoginForm(AuthenticationForm):

    username = forms.CharField(required=True,

                               widget=forms.TextInput(attrs={
                                   'placeholder':'Enter Username',
                                   'autocomplete':'username'
                               })
                               )

    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder':'Enter Password',
                                   'autocomplete':'new-password'

                               }))

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['profile_picture','college','graduation_year','skills']

        widgets = {
            'profile_picture': forms.FileInput(),
        }