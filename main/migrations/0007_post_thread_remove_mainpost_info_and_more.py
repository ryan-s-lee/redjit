# Generated by Django 4.2.4 on 2023-08-30 01:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_userdata_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now)),
                ('last_edit_time', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.userdata')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('comment_root', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.post')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.community')),
            ],
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='info',
        ),
        migrations.RemoveField(
            model_name='postinfo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postinfo',
            name='community',
        ),
        migrations.DeleteModel(
            name='CommentPost',
        ),
        migrations.DeleteModel(
            name='MainPost',
        ),
        migrations.DeleteModel(
            name='PostInfo',
        ),
    ]