from django.contrib import admin
from . models import Detail,Withdrawal,Deposit,Transaction,Withdrawal,Public_share,Active_share,Sold_share,Transfer,Promotion

# Register your models here.
class reg1(admin.ModelAdmin):
    list_display=('first_name','balance','phone','referal_income','date','inviter_name','inviter_phone','number')


class reg2(admin.ModelAdmin):
    list_display=('name','phone','amount','balance','date')


class reg3(admin.ModelAdmin):
    list_display=('name','phone','amount','inviter','date')


class reg4(admin.ModelAdmin):
    list_display=('phone','t_type','amount','date')


class reg5(admin.ModelAdmin):
    list_display=('phone','available','bought','remaining')


class reg6(admin.ModelAdmin):
    list_display=('name','shares_amount','shares_value','profit','period')

class reg7(admin.ModelAdmin):
    list_display=('name','shares_amount','shares_value','profit','period')


class reg8(admin.ModelAdmin):
    list_display=('sender','receiver','amount')

class reg9(admin.ModelAdmin):
    list_display=('name','phone','date')



admin.site.register(Detail , reg1)
admin.site.register(Withdrawal , reg2)
admin.site.register(Deposit , reg3)
admin.site.register(Transaction, reg4)
admin.site.register(Public_share, reg5)
admin.site.register(Active_share, reg6)
admin.site.register(Sold_share, reg7)

admin.site.register(Transfer,reg8)
admin.site.register(Promotion,reg9)

