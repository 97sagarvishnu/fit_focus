
from django.shortcuts import redirect, render
from django.http import HttpResponse
from.models import Trainers,otp

from .forms import AdmissionForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def trainers(request):
    dict_trainer={
        'trainers':Trainers.objects.all()
    }
    return render(request,'trainers.html',dict_trainer)


def admission(request):
  
  if request.method=="POST":
      print(request.method)
  form=AdmissionForm(request.POST)
  if form.is_valid():
      form.save()
      return render(request,'payment_form.html')
  form=AdmissionForm()
  dict_form={
      'form':form
  }
  return render(request,'admission.html', dict_form)





# def payment(request):
#     if request.method == 'POST':
#         person_name = request.POST.get('person_name')
#         card_number = request.POST.get('card_number')
#         expiry = request.POST.get('expiry')
#         cvv = request.POST.get('cvv')
#         # Create a new payment instance
#         payment = Payment.objects.create(
#             person_name=person_name,
#             card_number=card_number,
#             expiry=expiry,
#             cvv=cvv
#         )
#         # Redirect to a success page or perform further actions
#         return redirect('otp')

#     return render(request, 'payment.html')

# def payment(request):
#     # Example data (replace with actual data from payment gateway or form)
#     order_id = '12345'
#     transaction_id = 'ABC123XYZ'
#     amount = 1000.00
#     payment_status = 'Success'

#     # Create a Payment object and save it to the database
#     payment = Payment.objects.create(
#         order_id=order_id,
#         transaction_id=transaction_id,
#         amount=amount,
#         payment_status=payment_status
#     )

#     # Optionally, you can save the payment object explicitly
#     payment.save()

#     return render(request, 'payment.html')  
# from django.shortcuts import render, redirect
# from .models import Payment
# def payment_view(request):
#     if request.method == 'POST':
#         amount = request.POST['amount']
#         payment_method = request.POST['payment_method']
#         payment = payment.objects.create(amount=amount, payment_method=payment_method)
#         payment.save()
#         return redirect('payment_success')  # Redirect to success page

#     return render(request, 'payment_form.html')

# def payment_success(request):
#     return render(request, 'payment_success.html')

# def payment_failure(request):
#     return render(request, 'payment_failure.html')

from django.shortcuts import render

def payment_success(request):
    return render(request, 'payment_success.html')


def payment_failure(request):
    return render(request, 'payment_failure.html')

from django.shortcuts import render, redirect
from .models import Payment

def payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        if amount and payment_method:
            # Use the model class Payment, not a local variable payment
            payment = Payment.objects.create(amount=amount, payment_method=payment_method)
            return redirect('payment_success')  # Redirect to success page
        else:
            return redirect('payment_failure')  # Redirect to failure page if data is missing

    return render(request, 'payment_view.html')



def otp(request):
    if request.method == 'POST':
        # # Retrieve OTP code entered by the user
        # otp_code = ''.join(request.POST.getlist('otp'))
        
        # # Check if the entered OTP code exists in the database
        # if otp.objects.filter(code=otp_code).exists():
        #     messages.success(request, 'OTP verified successfully!')
      return redirect('confirmation.html')
    else:
            # messages.error(request, 'Invalid OTP. Please try again.')

       return render(request, 'otp.html')



def confirmation(request):
    return render(request,'confirmation.html')





