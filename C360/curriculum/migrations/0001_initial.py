# Generated by Django 4.2 on 2023-08-31 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resource', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='semister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1st year', '1st year'), ('2nd year', '2nd year'), ('3rd year', '3rd year'), ('4th year', '4th year'), ('5th year', '5th year')], default='1st year', max_length=50)),
                ('semister_number', models.CharField(choices=[('1st semister', '1st semister'), ('2nd semister', '2nd semister')], default='1st semister', max_length=50)),
                ('courses', models.ManyToManyField(to='resource.course')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.department')),
            ],
        ),
    ]