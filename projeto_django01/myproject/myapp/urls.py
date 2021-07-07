from django.urls import path
from . import views

urlpatterns = [
    path('', views.mvp, name='mvp'),
    path('home/', views.home, name='home')
]
