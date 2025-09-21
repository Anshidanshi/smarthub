from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import CustomUser
from django.db.models import Count
# Create your views here.
def StudentDashboard(request,pk):
    if request.user.username != pk:
        return HttpResponse('you don;t have the permission')
    user=CustomUser.objects.get(username=pk)
    #student=Achievement.objects.get(user=user)

    Achievements = Achievement.objects.filter(user=user)
    num_achievements = Achievements.filter(status='approved').count()
    pending_achievements = Achievements.filter(status='pending').count()
    rejected_achievements = Achievements.filter(status='rejected').count()
    print(num_achievements)
    print(pending_achievements)
    if num_achievements == 0:
        return HttpResponse("No achievement found")
    context = {
        'user': user,
        'num_achievements': num_achievements ,
        'pending_achievements': pending_achievements,
        'rejected_achievements': rejected_achievements,
    }
    return render(request,'student_dashbord.html',context)

def FacultyDashboard(request,pk):
    pass
