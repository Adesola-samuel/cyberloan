# Generated by Django 2.2.5 on 2020-05-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='applicant_income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='coapplicant_income',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='credit_history',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='loan_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='loan_amount_term',
            field=models.IntegerField(),
        ),
    ]
