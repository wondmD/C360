# Generated by Django 4.2.5 on 2023-09-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupapp', '0002_atachement'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='groupapp/static/resource'),
        ),
    ]