from django.db import models

# Create your models here.
CATAGRORY_CHOICES = [
    ('publication','Publication'),
    ('project','Project'),
    ('award','Award'),
    ('certification','Certification'),
    ('other','Other'),
]
STATUS_CHOICES = [
    ('pending','Pending'),
    ('approved','Approved'),
    ('rejected','Rejected'),
]
class Achievement(models.Model):
    user=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    completed_on=models.DateField(auto_now_add=True)
    document=models.FileField(upload_to='achievements/')
    category=models.CharField(max_length=100,choices=CATAGRORY_CHOICES,default='other')
    verified=models.BooleanField(default=False)
    faculty = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_achievements')
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending') # pending, approved, rejected
    def __str__(self):
        return self.title
class Subject(models.Model):
    name=models.CharField(max_length=100)
    credits=models.IntegerField()
    
    def __str__(self):
        return self.name

class Academic(models.Model):
    user=models.ForeignKey("accounts.CustomUser", verbose_name=(""), on_delete=models.CASCADE)
    subject=models.ForeignKey("Subject", verbose_name=(""), on_delete=models.CASCADE)
    cgpa=models.IntegerField()