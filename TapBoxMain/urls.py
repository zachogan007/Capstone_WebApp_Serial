from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.loginpage, name = 'login'),
    path('login/', TemplateView.as_view(template_name="TapBoxMain/login.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tapbox/', views.mainpage, name = 'mainpage'),
    path('logout/', views.logoutPage, name = 'logout'),

]


