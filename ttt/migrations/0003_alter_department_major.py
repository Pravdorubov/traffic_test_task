# Generated by Django 4.1.2 on 2022-10-30 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttt', '0002_alter_department_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ttt.department'),
        ),
    ]
