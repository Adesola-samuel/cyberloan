# Generated by Django 2.2.5 on 2020-05-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0009_remove_help_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='video',
            field=models.FileField(blank=True, upload_to='static/videos'),
        ),
    ]
