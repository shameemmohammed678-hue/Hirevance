from django.urls import path
from .import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('change_profile/',views.change_profile,name = 'change_profile'),
    path('settings/',views.settings_page,name='settings'),
    path('change_password/',views.change_password,name='change_password'),
    path('logout/',views.Logout,name = 'logout')
]