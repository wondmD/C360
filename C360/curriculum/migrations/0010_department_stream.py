# Generated by Django 4.2 on 2023-10-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0009_alter_semister_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='stream',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Engineering', 'Engineering')], default='Engineering', max_length=50),
        ),
    ]