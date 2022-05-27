from django.contrib import admin
from django.urls import path, include
from bootstrap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bootstrap.urls'), name = "home"),
    path('about/', views.about, name = 'about'),
    path('youtube/', views.youtube, name = 'youtube'),
    path('son/', views.son, name = 'son'),
    path('wpt/', views.wpt, name = 'wpt'),
]
