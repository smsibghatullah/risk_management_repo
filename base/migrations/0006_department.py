# Generated by Django 4.1.4 on 2023-05-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_auditprogramrepo_title_alter_riskrepo_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]