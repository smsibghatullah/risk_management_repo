from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class AuditProgramRepo(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)

class RiskRepo(models.Model):
   title = models.CharField(max_length=30, null=True, blank=True)
   department_name = models.CharField(max_length=30, null=True, blank=True)
   description = models.TextField()  