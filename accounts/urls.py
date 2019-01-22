from django.urls import path, include

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('edit_profile_pic', views.edit_profile_pic, name='edit_profile_pic'),
    path('login', views.login, name='login_user'),
    path('logout', views.logout, name='logout_user'),
    path('account_options/', include('django.contrib.auth.urls'))
]
