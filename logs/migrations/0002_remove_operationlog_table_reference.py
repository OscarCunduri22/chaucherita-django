# Generated by Django 5.0.2 on 2024-02-12 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationlog',
            name='table_reference',
        ),
    ]