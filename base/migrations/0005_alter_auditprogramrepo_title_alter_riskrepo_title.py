# Generated by Django 4.1.4 on 2023-05-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_riskrepo_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditprogramrepo',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='riskrepo',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]