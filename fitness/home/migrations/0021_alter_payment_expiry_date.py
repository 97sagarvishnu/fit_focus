# Generated by Django 5.0.1 on 2024-05-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_rename_expiry_payment_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
    ]
