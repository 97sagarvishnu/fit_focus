from collections import UserDict
from datetime import timezone
from django.db import models

class Trainers(models.Model):
   trainer_name=models.CharField(max_length=255)
   trainer_dept=models.CharField(max_length=255)
   trainer_image=models.ImageField(upload_to='trainers')
   
class Admission(models.Model):
   name=models.CharField(max_length=255)
   phone=models.CharField(max_length=10)
   email=models.EmailField()
   admission_date=models.DateField()
   
   
# class Payment(models.Model):
#    Person_name=models.CharField(max_length=20)
#    card_number=models.CharField(max_length=15)
#    expiry=models.DateField()
#    cvv=models.CharField(max_length=3)
   



# models.py

from django.db import models

# class Payment(models.Model):
#    #  order_id = models.CharField(max_length=100)
#     order_id = models.CharField(max_length=100, default='')

#    #  transaction_id = models.CharField(max_length=100)
#     transaction_id = models.CharField(max_length=100, default='')

#    #  amount = models.DecimalField(max_digits=10, decimal_places=2)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
 
#     payment_status = models.CharField(max_length=20, default='Pending')
#    #  person_name = models.CharField(max_length=100)
#     person_name = models.CharField(max_length=100, default='')
#     def __str__(self):
#         return self.order_id


# from django.db import migrations, models

# class Migration(migrations.Migration):

#     dependencies = [
#         ('your_app_name', '0001_initial'),  # Replace with your actual initial migration
#     ]

#     operations = [
#         migrations.AddField(
#             model_name='payment',
#             name='amount',
#             field=models.DecimalField(max_digits=10, decimal_places=2),
#         ),
#         migrations.AddField(
#             model_name='payment',
#             name='order_id',
#             field=models.CharField(max_length=100),
#         ),
#         migrations.AddField(
#             model_name='payment',
#             name='payment_status',
#             field=models.CharField(max_length=20, default='Pending'),
#         ),
#         migrations.AddField(
#             model_name='payment',
#             name='transaction_id',
#             field=models.CharField(max_length=100),
#         ),
#     ]



class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    payment_method = models.CharField(max_length=20,default='')  # 'card' or 'upi'
    payment_date = models.DateTimeField(default='2024-05-09 01:29:00')
    # Add more fields as needed
    def get_default_payment_date():
        return timezone.now()


class otp(models.Model):
    code = models.CharField(max_length=4)

    