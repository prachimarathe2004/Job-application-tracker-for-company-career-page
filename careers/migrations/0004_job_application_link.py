# Generated by Django 5.1.4 on 2025-07-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0003_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='application_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
