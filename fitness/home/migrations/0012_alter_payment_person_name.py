# Generated by Django 5.0.1 on 2024-04-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_payment_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='person_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
