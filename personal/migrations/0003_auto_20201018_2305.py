# Generated by Django 2.2.5 on 2020-10-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20201018_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='about_me',
            field=models.CharField(default='', max_length=150),
        ),
    ]
