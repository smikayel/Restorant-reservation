# Generated by Django 3.2.2 on 2021-05-18 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_userprofile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='number',
        ),
    ]
