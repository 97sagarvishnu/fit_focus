from django.contrib import admin
from.models import Trainers,Admission,Payment,otp


admin.site.register(Trainers)

admin.site.register(otp)





# class PaymentAdmin(admin.ModelAdmin):
#     list_display=('person_name','Payment_status')
#     list_filter = ('payment_status',)
#     admin.site.register(Payment)



class AdmissionAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','admission_date')
    admin.site.register(Admission)


# admin.py


# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('order_id', 'transaction_id', 'amount', 'payment_status', 'person_name')
#     list_filter = ('payment_status',)  # Optional: add filter options
#     search_fields = ('order_id', 'person_name')  # Optional: add search fields

# admin.site.register(Payment, PaymentAdmin)
# from django.contrib import admin
# from .models import Payment

admin.site.register(Payment)
