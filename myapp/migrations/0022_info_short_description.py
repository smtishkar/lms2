# Generated by Django 5.0.3 on 2024-08-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_content_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='short_description',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]