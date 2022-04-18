from django.db import models

# Create your models here.


class LNMOnline(models.Model):
    CheckoutRequestID = models.CharField(max_length=50, default='none')
    MerchantRequestID = models.CharField(max_length=50, default='none')
    ResultCode =  models.IntegerField(default=0)
    ResultDesc = models.CharField(max_length=120 ,default='none')
    Amount = models.IntegerField(default=0)
    MpesaReceiptNumber = models.CharField(max_length=15, default='none')
    
    TransactionDate = models.DateTimeField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=50, default=0)


    def __str__(self):
        return self.PhoneNumber
    
    
class C2BPayments(models.Model):
    TransactionType= models.CharField(max_length=15, default='none')
    TransID= models.CharField(max_length=15, default='none')
    TransTime=  models.CharField(max_length=15, default='none')
    TransAmount = models.CharField(max_length=15, default='none')
    BusinessShortCode = models.IntegerField(default=0)
    BillRefNumber = models.CharField(max_length=15, default='none')
    TransTime=  models.CharField(max_length=15, default='none')
    InvoiceNumber = models.CharField(max_length=25, default='none')
    OrgAccountBalance = models.CharField(max_length=15, default='none')
    ThirdPartyTransID = models.CharField(max_length=25, default='none')
    MSISDN =  models.CharField(max_length=15, default='none') 
    FirstName =  models.CharField(max_length=25, default='none')
    MiddleName = models.CharField(max_length=25, default='none')
    LastName = models.CharField(max_length=25, default='none') 
    TransactionDate = models.DateTimeField(blank=True, null=True)



    



