from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Lessons.as_view(), name="Lessons"),
]