# Generated by Django 5.0.3 on 2024-11-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_remove_edu_programs_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='edu_programs',
            name='cert_requirements',
            field=models.CharField(default=123, max_length=250),
            preserve_default=False,
        ),
    ]