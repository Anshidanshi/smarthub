from django.db import models

# Create your models here.
CATAGRORY_CHOICES = [
    ('publication','Publication'),
    ('project','Project'),
    ('award','Award'),
    ('certification','Certification'),
    ('other','Other'),
]

class Achievement(models.Model):
    user=models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    completed_on=models.DateField(null=True,blank=True)
    document=models.FileField(upload_to='achievements/')
    category=models.CharField(max_length=100,choices=CATAGRORY_CHOICES,default='other')
    
    def __str__(self):
        return self.title
    