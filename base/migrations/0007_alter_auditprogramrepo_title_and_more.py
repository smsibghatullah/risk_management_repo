# Generated by Django 4.1.4 on 2023-05-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditprogramrepo',
            name='title',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='riskrepo',
            name='department_name',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='riskrepo',
            name='title',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
