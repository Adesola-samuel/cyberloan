# Generated by Django 2.2.5 on 2020-10-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0015_auto_20201019_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='color',
            field=models.CharField(blank=True, default='', max_length=35, null=True),
        ),
    ]
