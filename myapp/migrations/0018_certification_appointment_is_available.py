# Generated by Django 5.0.3 on 2024-05-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_certification_appointment_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification_appointment',
            name='is_available',
            field=models.BooleanField(blank=True, default=1),
        ),
    ]