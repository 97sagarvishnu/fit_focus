# Generated by Django 5.0.1 on 2024-05-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_payment_expiry_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='expiry_date',
            new_name='expiry',
        ),
    ]
