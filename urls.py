from django.urls import path
from . import views
urlpatterns = [
  path('',views.login,name='login'),
  path('login',views.login,name='login'),
  path('loginlogic',views.loginlogic,name='loginlogic'),
  path('dashboard',views.dashboard,name='dashboard'),
  path('searchstudent',views.searchstudent,name='searchstudent'),
  path('searchstu',views.searchstu,name='searchstu'),
  path('logout',views.logout,name='logout'),
  ]