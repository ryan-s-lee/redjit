# Generated by Django 4.2.4 on 2023-08-27 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_commentpost_mainpost_postinfo_alter_community_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='username',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='communities',
            field=models.ManyToManyField(blank=True, to='main.community'),
        ),
    ]