# Generated by Django 4.2.5 on 2023-09-20 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_alter_department_school'),
        ('main', '0004_remove_myusers_department_myusers_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myusers',
            name='department',
        ),
        migrations.AddField(
            model_name='myusers',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.department'),
        ),
    ]
