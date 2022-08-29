"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""devproject/urls.py"""
from django.contrib import admin
from django.urls import path
from mywebsite import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    #user
    path('', views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('deleteuser/', views.delete_user, name='deleteuser'),
    path('changeuserpassword/', views.change_user_password,name='changeuserpassword'),
    #Authentication
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('signin_promt/',views.signin_promt, name='signin_promt'),
    # Games
    path('snakegame/',views.snake_game, name='snakegame'),
    path('ponggame/',views.pong_game, name='ponggame'),
    path('2048game/',views.the_2048_game, name='2048game')
]