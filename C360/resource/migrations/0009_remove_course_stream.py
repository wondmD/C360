# Generated by Django 4.2 on 2023-10-24 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0008_remove_course_course_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='stream',
        ),
    ]
