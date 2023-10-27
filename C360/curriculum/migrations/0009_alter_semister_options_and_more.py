# Generated by Django 4.2 on 2023-10-17 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0008_level_remove_semister_courses_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semister',
            options={'ordering': ['year', 'semister_number']},
        ),
        migrations.AlterUniqueTogether(
            name='semister',
            unique_together={('year', 'semister_number')},
        ),
    ]
