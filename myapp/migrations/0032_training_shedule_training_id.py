# Generated by Django 5.0.3 on 2024-05-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_training_shedule_dlr_training_shedule_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='training_shedule',
            name='training_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]