# Generated by Django 5.0.1 on 2024-05-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_payment_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='my_char_field',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]
