# Generated by Django 5.0.1 on 2024-05-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_payment_person_name_payment_card_number_payment_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry',
            field=models.DateField(default='2024-12-31', max_length=5),
        ),
    ]
