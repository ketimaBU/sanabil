# Generated by Django 2.0.9 on 2019-02-09 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_necessiteux_appartient_centre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='necessiteux',
            name='pointure',
            field=models.IntegerField(blank=True, default=36, null=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(20)]),
        ),
    ]
