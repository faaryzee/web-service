# Generated by Django 5.0.1 on 2024-01-16 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departemens', '0001_initial'),
        ('kantors', '0010_alter_kantor_departemen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kantor',
            name='departemen',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='departemens.departemen'),
        ),
    ]
