from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('risk_repo', views.getRiskData),
    path('audit_program_repo', views.getAuditProgramData),
]