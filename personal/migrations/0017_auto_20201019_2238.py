# Generated by Django 2.2.5 on 2020-10-19 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20201019_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='logo',
        ),
    ]