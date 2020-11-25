from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('addUser/', Record, name="register"),
    path('home/', home, name="home"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    ]