# Generated by Django 5.0.1 on 2024-05-08 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_payment_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_method',
        ),
    ]
