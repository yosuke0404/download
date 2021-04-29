from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.download_video, name='download'),
    path('downloaded/', views.download_local, name='downloaded'),
]