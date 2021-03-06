# Generated by Django 2.2.5 on 2020-10-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_auto_20201019_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='skills', to='personal.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
