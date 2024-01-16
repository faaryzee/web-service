# Generated by Django 5.0.1 on 2024-01-16 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kantors', '0014_kantor_departemen'),
        ('karyawans', '0005_remove_review_kantor'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='kantor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='karyawans', to='kantors.kantor'),
            preserve_default=False,
        ),
    ]
