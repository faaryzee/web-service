# Generated by Django 5.0.1 on 2024-01-16 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kantors', '0007_alter_kantor_departemen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kantor',
            name='departemen',
        ),
    ]
