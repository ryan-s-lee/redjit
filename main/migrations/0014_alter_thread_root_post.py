# Generated by Django 4.2.4 on 2023-08-31 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_post_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='root_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.post'),
        ),
    ]