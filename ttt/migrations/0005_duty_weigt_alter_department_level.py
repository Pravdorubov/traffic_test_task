# Generated by Django 4.1.2 on 2022-10-30 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0004_alter_duty_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='weigt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='level',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
