# Generated by Django 3.2.2 on 2021-05-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_remove_userprofile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=50)),
                ('table_picture', models.ImageField(upload_to='hall_one_tables')),
                ('price', models.IntegerField()),
                ('discription', models.CharField(max_length=1000)),
                ('reserved', models.BooleanField()),
            ],
        ),
    ]
