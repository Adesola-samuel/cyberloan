# Generated by Django 2.2.5 on 2020-08-31 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0017_auto_20200831_1329'),
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
            name='dependents',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='education',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='gender',
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
        migrations.AlterField(
            model_name='prediction',
            name='loan_status',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='married',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='property_area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='self_employed',
            field=models.IntegerField(),
        ),
    ]
