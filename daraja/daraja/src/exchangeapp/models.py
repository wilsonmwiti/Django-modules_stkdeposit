from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Detail(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    first_name =models.CharField(max_length=30 , default='none')
    last_name =models.CharField(max_length=30 , default='none')
    email =models.CharField(max_length=100 , default='none')
    balance = models.IntegerField(default=0)
    username = models.CharField(max_length=30 , default='none')
    phone_code = models.CharField(max_length=30 , default='none')
    phone =models.CharField(max_length=30 , default='none')
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    staff  = models.BooleanField(default=False)
    verified  = models.BooleanField(default=False)
    invest1  = models.BooleanField(default=False)
    buy1  = models.BooleanField(default=False)
    r_link = models.CharField(max_length=30 , default='none')
    password =  models.CharField(max_length=30 , default='none')
    inviter_name =  models.CharField(max_length=30 , default='none')
    
    shares_income = models.IntegerField(default=0)
    referal_income = models.IntegerField(default=0)
    total_deposits = models.IntegerField(default=0)
    total_income = models.IntegerField(default=0)
    inviter_link = models.CharField(max_length=30 , default='none')
    inviter_phone = models.CharField(max_length=30 , default='none')
    total_promo = models.IntegerField(default=0)
    shares_status  = models.BooleanField(default=False)
    
    number = models.IntegerField(default=1)
    v_code = models.IntegerField(default=2134)

    def __str__(self):
        return self.user.username
   
   
class Withdrawal(models.Model):
    name = models.CharField(max_length=30 , default='none')
    phone = models.CharField(max_length=30 , default='none')
    balance = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    ref = models.CharField(max_length=30 , default='none')
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)


class Public_share(models.Model):
    name = models.CharField(max_length=30 , default='none')
    phone = models.CharField(max_length=30 , default='none')
    available = models.IntegerField(default=0)
    bought = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)
    span   = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)

class Deposit(models.Model):
    name = models.CharField(max_length=30 , default='none')
    phone = models.CharField(max_length=30 , default='none')
    amount = models.IntegerField(default=0)
    inviter_earned = models.IntegerField(default=0)
    inviter = models.CharField(max_length=30 , default='none')
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)


class Transaction(models.Model):
    detail = models.ForeignKey(Detail,null=True ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=30 , default='none')
    t_type = models.CharField(max_length=30 , default='none')
    amount = models.IntegerField(default=0)
    ref = models.CharField(max_length=30 , default='none')
    date = models.DateTimeField(auto_now_add=True)


class Active_share(models.Model):
    detail = models.ForeignKey(Detail,null=True ,on_delete=models.CASCADE)

    name = models.CharField(max_length=30 , default='none')
    phone = models.CharField(max_length=30 , default='none')
    shares_amount =  models.IntegerField(default=0)
    shares_value = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    period = models.CharField(max_length=30 , default='none')
    status   = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

class Sold_share(models.Model):
   
    name = models.CharField(max_length=30 , default='none')
    shares_amount =  models.IntegerField(default=0)
    shares_value = models.IntegerField(default=0)
    sale_amount = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    period = models.CharField(max_length=30 , default='none')
    status   = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
   


class Transfer(models.Model):
    sender = models.IntegerField(default=0)
    receiver = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)


class Promotion(models.Model):
    detail = models.ForeignKey(Detail,null=True ,on_delete=models.CASCADE)
    phone = models.CharField(max_length=30 , default='none')
    name = models.CharField(max_length=30 , default='none')
    email = models.CharField(max_length=500 , default='none')
    date = models.DateTimeField(auto_now_add=True)