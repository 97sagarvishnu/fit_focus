from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('trainers/', views.trainers, name='trainers'),
    path('admission/', views.admission, name='admission'),
    # path('payment/', views.payment, name='payment'),
    path('payment/', views.payment_view, name='payment_view'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failure/', views.payment_failure, name='payment_failure'),
    path('otp/', views.otp, name='otp')
#     path('otp/confirmation.html', views.confirmation, name='confirmation'),
# ]
]
