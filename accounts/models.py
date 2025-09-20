from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
# Create your models here.
Role_choice = [
    ('admin','Admin'),
    ('student','Student'),
    ('faculty','Faculty'),
    
]
class CustomUser(AbstractUser):
    #imag=models.ImageField()
    
    role=models.CharField(max_length=50,choices=Role_choice,default='student')
    email=models.EmailField(unique=True)
    
    #student
    reg_no=models.CharField(max_length=20,null=True,blank=True,unique=True)
    course=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    year_of_study=models.CharField(max_length=20,null=True,blank=True)
    
    #faculty
    employee_id=models.CharField(max_length=20,null=True,blank=True,unique=True)
    faculty_department=models.CharField(max_length=100,null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    
    def _str__(self):
        return f"{self.get_full_name()} -{self.role}"
    
    
        
    
class StudentManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='student')
class StudentProfile(CustomUser):
    objects=StudentManger()
    class Meta:
        proxy=True

class FacultyManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='faculty')

class FacultyProfile(CustomUser):
    objects = FacultyManger()
    class Meta:
        proxy=True
    
