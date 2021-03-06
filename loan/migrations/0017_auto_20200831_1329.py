# Generated by Django 2.2.5 on 2020-08-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0016_auto_20200608_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='applicant_income',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='coapplicant_income',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='credit_history',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='dependents',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='education',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='gender',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='loan_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='loan_amount_term',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='loan_status',
            field=models.FloatField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='married',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='property_area',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='self_employed',
            field=models.FloatField(),
        ),
    ]
