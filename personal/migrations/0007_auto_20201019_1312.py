# Generated by Django 2.2.5 on 2020-10-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20201018_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='yrs_exp',
        ),
        migrations.AddField(
            model_name='biodata',
            name='freelance',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='highest_qualification',
            field=models.TextField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='biodata',
            name='started_work',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]