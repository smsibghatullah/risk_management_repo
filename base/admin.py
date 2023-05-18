from django.contrib import admin

from base.models import AuditProgramRepo, RiskRepo

# Register your models here.
admin.site.register(RiskRepo)
admin.site.register(AuditProgramRepo)