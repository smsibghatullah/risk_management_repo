from django.contrib import admin
from django.forms import Select

from base.models import AuditProgramRepo, RiskRepo, Department

class DetailsAdmin(admin.ModelAdmin):
    # fields = ('title', 'department_name', 'description')
    def cube(num, two):
      return [two, two]
    def get_form(self, request, obj=None, **kwargs):
        # 1. Get the form from the parent class:
        form = super(DetailsAdmin, self).get_form(request, obj, **kwargs)
        # 2. Change the widget:
        org_list = Department.objects.all()
        form.base_fields['department_name'].widget = Select(choices=list(map(self.cube, org_list)) )
        # 3. Return the form!
        return form

# Register your models here.
admin.site.register(RiskRepo, DetailsAdmin)
admin.site.register(AuditProgramRepo,DetailsAdmin)
admin.site.register(Department)