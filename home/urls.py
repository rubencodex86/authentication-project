from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.login_request, name='login_request'),
    # path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    # path('/logout', views.logout_request, name='logout_request'),
    path('', views.logout_request, name='logout_request'),
]
