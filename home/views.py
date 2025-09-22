from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import CustomUser
from django.db.models import Count
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
def StudentDashboard(request,pk):
    if request.user.username != pk:
        return HttpResponse('you don;t have the permission')
    user=CustomUser.objects.get(username=pk)
    #student=Achievement.objects.get(user=user)

    Achievements = Achievement.objects.filter(user=user)
    dashboard_stud = Achievements.order_by('-date')[:4]
    num_achievements = Achievements.filter(status='approved').count()
    pending_achievements = Achievements.filter(status='pending').count()
    rejected_achievements = Achievements.filter(status='rejected').count()
    print(num_achievements)
    print(pending_achievements)
    
    academics=Academic.objects.get(user=user)
    Subjects=academics.Subject.all()
    print(Subjects)
    
    if num_achievements == 0:
        return HttpResponse("No achievement found")
    context = {
        'user': user,
        'Achievements':dashboard_stud,
        'num_achievements': num_achievements ,
        'pending_achievements': pending_achievements,
        'rejected_achievements': rejected_achievements,
        'academics':academics,
    }
    return render(request,'student_dashbord.html',context)

class ActivityUpload(LoginRequiredMixin,CreateView):
    model = Achievement
    fields = ['title', 'description', 'date', 'document', 'category']
    template_name = 'acctivity_tracker.html'
    #success_url = reverse_lazy('home:home', kwargs={'pk': request.user.username})
    
    def get_success_url(self):
        return reverse_lazy('home:home', kwargs={'pk': self.request.user.username})
    def form_valid(self, form):
        achieve = form.save(commit=False)
        achieve.user = self.request.user
        achieve.save()
        return super().form_valid(form)
class CertificateView(LoginRequiredMixin,ListView):
    model = Achievement
    template_name = 'certification.html'
    context_object_name = 'certificates'
    def get_queryset(self):
        return Achievement.objects.filter(user=self.request.user).order_by('-date')

def FacultyDashboard(request,pk):
    pass
