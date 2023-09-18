# Generated by Django 4.2.1 on 2023-09-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_delete_departmentsemester'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.CharField(choices=[('School of Applied Natural Sciences', 'School of Applied Natural Sciences'), ('School of Civil Engineering and Architecture', 'School of Civil Engineering and Architecture'), ('School of Electrical Engineering and Computing', 'School of Electrical Engineering and Computing'), ('School of Mechanical, Chemical, and Materials Engineering', 'School of Mechanical, Chemical, and Materials Engineering')], default='School of Electrical Engineering and Computing', max_length=100),
        ),
    ]