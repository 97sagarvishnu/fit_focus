# Generated by Django 5.0.1 on 2024-05-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_payment_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
    ]
