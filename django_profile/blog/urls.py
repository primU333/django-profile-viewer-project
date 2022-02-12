from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('login/', views.login_view, name='blog-login'),
    path('home/', views.home, name='blog-main-page'),
    path('logout/', views.logout_veiw, name='blog-logout'),
]