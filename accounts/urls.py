from .views import *
from django.urls import path
from . import views
urlpatterns = [
    path('registration/student/',StudentCreation.as_view(),name="stude"),
    path('registration/faculty/',FacultyCreation.as_view(),name='faculty'),
    path('login',views.login_,name="login"),
]
