from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login as login_auth
from django.contrib import messages
# Create your views here.
class StudentCreation(CreateView):
    model=CustomUser
    fields=['username','email','password','first_name','last_name','reg_no','course','department','year_of_study']
    template_name='registration.html'
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        user=form.save(commit=False)
        user.role='student'
        user.password=make_password(form.cleaned_data["password"])
        user.is_approved=True
        user.save()
        return super().form_valid(form)

class FacultyCreation(LoginRequiredMixin,CreateView):
    model=CustomUser
    fields=['username','email','password','first_name','last_name','employee_id','faculty_department','designation']
    template_name='registrationfa.html'
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        if CustomUser.objects.filter(username=form.cleaned_data['username']).exists():
            form.add_error('username', 'This username is already used!')
            return self.form_invalid(form)
        if CustomUser.objects.filter(email=form.cleaned_data['email']).exists():
            form.add_error('email', 'This email is already used!')
            return self.form_invalid(form)
        
        user=form.save(commit=False)
        user.role='faculty'
        user.password=make_password(form.cleaned_data["password"])
        user.is_apporved=True
        user.is_staff=True
        user.save()
        return super().form_valid(form)
    

def login_(request):
    if request.user.is_authenticated:
        
        return HttpResponse(f"welcome {request.user.username}")
    if request.method == "POST":
        username = request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_auth(request,user)
            messages.success(request, f"welcome {user.username}")
            
            if user.role=='student':
                return HttpResponse(f"welcome student {user.username}")
            else:
                return HttpResponse("ksdf")
        else:
            messages.error(request, f"invalid username or password")
    return render(request, 'login.html')