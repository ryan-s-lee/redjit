# Generated by Django 4.2.4 on 2023-08-30 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_post_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.post'),
        ),
    ]