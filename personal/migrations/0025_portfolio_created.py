# Generated by Django 2.2.5 on 2020-10-22 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0024_auto_20201021_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]