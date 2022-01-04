from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('login/', views.login, name='blog-login'),
    path('home/', views.home, name='blog-main-page'),
]