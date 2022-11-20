from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('login/', views.loginpage, name = 'login'),
    path('tapbox/', views.mainpage, name = 'mainpage'),
    path('logout/', views.logoutPage, name = 'logout'),
]