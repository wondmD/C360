# Generated by Django 4.2.2 on 2023-08-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_alter_resource_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='crh',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
