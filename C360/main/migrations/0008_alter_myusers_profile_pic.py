# Generated by Django 4.2.5 on 2023-10-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_myusers_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to='profilepic'),
        ),
    ]
