# Generated by Django 3.1.7 on 2021-03-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatable_null_vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatable',
            name='payment_type',
        ),
    ]