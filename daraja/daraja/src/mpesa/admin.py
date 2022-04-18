from django.contrib import admin
from . models import LNMOnline,C2BPayments
# Register your models here.


class reg1(admin.ModelAdmin):
    list_display=('MpesaReceiptNumber','Amount','PhoneNumber','TransactionDate')

class reg2(admin.ModelAdmin):
    list_display=('FirstName','TransID','TransAmount','MSISDN','date','OrgAccountBalance')

admin.site.register(LNMOnline , reg1)
admin.site.register(C2BPayments, reg2)
    



    
