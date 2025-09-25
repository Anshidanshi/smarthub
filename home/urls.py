from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('student/<str:pk>', views.StudentDashboard, name='home'),
    path('ActivityUpload/', views.ActivityUpload.as_view(), name='activity_upload'),
    path('certificates/', views.CertificateView.as_view(), name='certificates'),
    path('certificate/<int:pk>/', views.CertificatView.as_view(), name='certificate_detail'),
    path('certificate/<int:pk>/update/', views.CertificateUpdateView.as_view(), name='certificate_update'),
]

