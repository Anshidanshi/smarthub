from django.urls import path
from . import views

urlpatterns = [
    path('student/<str:pk>', views.StudentDashboard, name='home')
]

