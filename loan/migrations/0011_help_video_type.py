# Generated by Django 2.2.5 on 2020-05-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0010_help_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='video_type',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]