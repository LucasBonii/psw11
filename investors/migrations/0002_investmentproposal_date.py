# Generated by Django 5.1 on 2024-08-16 17:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentproposal',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
