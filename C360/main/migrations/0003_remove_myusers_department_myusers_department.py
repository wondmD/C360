# Generated by Django 4.2.1 on 2023-09-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_delete_departmentsemester'),
        ('main', '0002_myusers_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myusers',
            name='department',
        ),
        migrations.AddField(
            model_name='myusers',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.department'),
        ),
    ]
