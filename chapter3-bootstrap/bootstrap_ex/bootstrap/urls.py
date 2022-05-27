from django.urls import path, include
from bootstrap import views

urlpatterns = [
    path('', views.home, name ='home')
]
