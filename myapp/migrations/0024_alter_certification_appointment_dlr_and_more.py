# Generated by Django 5.0.3 on 2024-05-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_dealers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification_appointment',
            name='dlr',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='certification_appointment',
            name='employee_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='certification_appointment',
            name='employee_last_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='certification_appointment',
            name='employee_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]