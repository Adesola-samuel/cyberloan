# Generated by Django 2.2.5 on 2020-10-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_archive'),
        ('personal', '0025_portfolio_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='achieves',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
