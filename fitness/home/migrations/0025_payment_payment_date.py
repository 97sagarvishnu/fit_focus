# Generated by Django 5.0.1 on 2024-05-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_payment_amount_alter_payment_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default='2024-05-08 08:30:00'),
            preserve_default=False,
        ),
    ]
