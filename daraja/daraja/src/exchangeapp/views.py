from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import F,Sum
from django.core.files.storage import FileSystemStorage
from django.db.models.query import QuerySet
from . models import Detail,Withdrawal,Transaction,Deposit,Public_share,Active_share,Sold_share,Transfer,Promotion
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def homepage(request):
    return render(request , "homepage.html")

def profile(request):
    return render(request , "profile.html")

def depositn(request):
    return render(request , "deposit.html")

def dashboard(request):
    if request.user.is_authenticated:
        phone = request.user.detail.phone

        c =  Detail.objects.get(phone=phone)

        


        share =  Public_share.objects.get(name="none")
       

        shares= c.active_share_set.last()

        
        

        x = c.verified

        if x ==True:

            
            return render(request , "dashboard.html",{'share': share,'shares': shares} )

        else:
            return redirect("v_code")

def dashboard2(request):
    if request.user.is_authenticated:
        phone = request.user.detail.phone

        share =  Public_share.objects.get(name="none")

        c =  Detail.objects.get(phone=phone)
        x = c.verified

        

        shares= c.active_share_set.last()


        if x ==True:
            messages.info(request, 'Follow instructions sent to your phone to complete payment.You can also pay via paybill 4048415' , extra_tags='success')

            return render(request , "deposit.html")

        else:
            return redirect("v_code")
#VERIFICATION PAGE



   
def v_code(request):
    if request.method == 'POST':

      
        if request.user.is_authenticated:
            phone = request.user.detail.phone

            c =  Detail.objects.get(phone=phone)
            x = c.verified
            code = int(c.v_code)

            if x== True:
                messages.info(request,  'Phone number already verified', extra_tags='warning')
                return redirect("dashboard")


            else:
                code1 = int(request.POST['code'])
                if code == code1:
                    Detail.objects.filter(phone=phone).update(verified=True)
                    messages.info(request,  'Your phone number has been verified.', extra_tags='success')

                    return redirect("dashboard")


                else:
                    messages.info(request,  'Wrong verification code', extra_tags='warning')

                    return redirect("v_code")
        else:

            messages.info(request,  'Please login first', extra_tags='warning')

            return redirect("login")

            
            



    else:
        
        return render(request , "verify.html")

#RESEND VERIFICATION CODE

def resend_code(request):
    if request.user.is_authenticated:
        phone = request.user.detail.phone

        c =  Detail.objects.get(phone=phone)
        x = c.verified
        phone_code = str(c.phone_code)

        send_to_phone = "+" + phone_code

        if x ==False:

            import random

            v_code = random.randint(1000,9999)

            v_code = str(v_code)

            Detail.objects.filter(phone=phone).update(v_code=v_code)



            #resend code

                
            import http.client


            #access token

            from urllib.request import urlopen
            import json
            conn = http.client.HTTPSConnection("auth.routee.net")

            payload = "grant_type=client_credentials"

            headers = {
                'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                'content-type': "application/x-www-form-urlencoded"
                }

            conn.request("POST", "/oauth/token", payload, headers)

            res = conn.getresponse()
            data = res.read()


            data = data.decode("utf-8")

            json_obj = json.loads(data)

            access_token = (json_obj['access_token']) # prints the string with 'source_name' key




            #send msg
            code = v_code

            phone = send_to_phone

            

            msg =   "Your StockExchange verification code is " + code

            conn = http.client.HTTPSConnection("connect.routee.net")

            payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



            headers = {
                'authorization': "Bearer "+access_token+"",
                'content-type': "application/json"
                }


            conn.request("POST", "/sms", payload, headers)


            res = conn.getresponse()
            data = res.read()
            messages.info(request,  'Code sent successfully', extra_tags='success')
            return redirect("v_code")

        else:
            return redirect("dashboard")


#EDIT PHONE NUMBER

def edit_phone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            phone1 = request.user.detail.phone

            c =  Detail.objects.get(phone=phone1)
            x = c.verified
            

            if x ==False:
                
                phone = request.POST['phone']
                phone_digits= len(phone)

                if phone_digits != 10 or phone_digits>10:
                    messages.info(request, 'Invalid phone number,please use the format 07xx or 01xxx', extra_tags='warning')

                    return redirect("v_code")

                if phone == phone1:
                    messages.info(request, 'No changes made', extra_tags='warning')

                    return redirect("v_code")

                else:

                    phone_code = str(+254) + phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9]

                    Detail.objects.filter(phone=phone1).update(phone=phone)
                    Detail.objects.filter(phone=phone1).update(phone_code=phone_code)
                    User.objects.filter(username=phone1).update(username=phone)


                    #generate code

                    import random

                    v_code = random.randint(1000,9999)

                    v_code = str(v_code)

                    Detail.objects.filter(phone=phone).update(v_code=v_code)



                    #resend code

                        
                    import http.client


                    #access token

                    from urllib.request import urlopen
                    import json
                    conn = http.client.HTTPSConnection("auth.routee.net")

                    payload = "grant_type=client_credentials"

                    headers = {
                        'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                        'content-type': "application/x-www-form-urlencoded"
                        }

                    conn.request("POST", "/oauth/token", payload, headers)

                    res = conn.getresponse()
                    data = res.read()


                    data = data.decode("utf-8")

                    json_obj = json.loads(data)

                    access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                    #send msg
                    code = v_code

                    phone = phone_code

                    

                    msg =   "Your StockExchange verification code is " + code

                    conn = http.client.HTTPSConnection("connect.routee.net")

                    payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                    headers = {
                        'authorization': "Bearer "+access_token+"",
                        'content-type': "application/json"
                        }


                    conn.request("POST", "/sms", payload, headers)


                    res = conn.getresponse()
                    data = res.read()

                    messages.info(request, 'Phone number updated successfully', extra_tags='success')
                    return redirect("v_code")
            else:
                return redirect("dashboard")

                            







    else:

        return redirect("dashboard")



#LOGIN SECTION
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            user = auth.authenticate(username= username, password=password)
            if user is not None:

                auth.login(request , user)


                phone = request.user.detail.phone

                c =  Detail.objects.get(phone=phone)
        
                x = c.verified

                if x == False:

                    return redirect('v_code')
                
                else:

                    return redirect('dashboard')
            
                
            else:
                
                messages.info(request, 'Wrong Password', extra_tags='warning')
                return render(request , 'login.html',{'username': username,'password':password})

        else:
                
            messages.info(request,  'Wrong Username', extra_tags='warning')
            return render(request , 'login.html',{'username': username,'password':password})
    else:
         
        return render(request , 'login.html')

def login2(request, i_link='0000'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            user = auth.authenticate(username= username, password=password)
            if user is not None:

                auth.login(request , user)


                phone = request.user.detail.phone

                c =  Detail.objects.get(phone=phone)
        
                x = c.verified

                if x == False:

                    return redirect('v_code')
                
                else:

                    return redirect('dashboard')
            
                
            else:
                
                messages.info(request, 'Wrong Password', extra_tags='warning')
                return render(request , 'login.html',{'username': username,'password':password})

        else:
                
            messages.info(request,  'Wrong Username', extra_tags='warning')
            return render(request , 'login.html',{'username': username,'password':password})
    else:
         
        return render(request , 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request, i_link='0000'):
    if request.method == "POST":
        name1 = request.POST["first_name"]
        name2 = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["username"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]

        name1= name1.capitalize()
        name2= name2.capitalize()

        if pass1 == pass2:
            pass_length= len(pass1)
            phone_digits= len(phone)

            exist = Detail.objects.filter(r_link=i_link).exists()


           

            if User.objects.filter(username=phone).exists():
                messages.info(request, 'Phone  Number Used', extra_tags='warning')
                return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Used', extra_tags='warning')
                return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})

            elif pass_length<4:
                messages.info(request, 'Your password should contain more than 4 digits', extra_tags='warning')
                return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})
            
            elif phone_digits != 10 or phone_digits>10:
                messages.info(request, 'Invalid phone number,please use the format 07xx or 01xxx', extra_tags='warning')
                return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})
            
            

            elif  exist== False:
                messages.info(request, 'Invalid referral link', extra_tags='warning')
                return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})

                
                

        

                
            else:

                #inviter details
                c =  Detail.objects.get(r_link=i_link)

                inviter_name = c.first_name

                inviter_phone= c.phone


                #number


                link_owner = Detail.objects.last()
                

                number = link_owner.number

                
                number= number + 1

                #generate verification code

                phone_code = str(+254) + phone[1] + phone[2] + phone[3] + phone[4] + phone[5] + phone[6] + phone[7] + phone[8] + phone[9]
                    

                import random
                v_code = random.randint(1000,9999)

                v_code = str(v_code)


                

                #generate referral link

                                

                import string
                string.ascii_letters
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                import random
                a =random.choice(string.ascii_letters)
                a = a.upper()



                import random

                b = str(random.randint(10,99))

                string.ascii_letters
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                import random
                c =random.choice(string.ascii_letters)
               

                d = str(random.randint(100,999))

                string.ascii_letters
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                import random
                e =random.choice(string.ascii_letters)

                

                



                r_link = "l" +a + b + c +d + e  + str(number)




                c =  Detail.objects.get(r_link=i_link)

                new2_save = Promotion(detail=c,name=name1,phone=phone)
                new2_save.save()
                
                Detail.objects.filter(r_link=i_link).update(total_promo= F('total_promo') + 1)









                user = User.objects.create_user(username=phone,first_name=name1,last_name=name2,password=pass1,email=email)
                user.save()
                add = Detail(user=user,phone=phone,first_name=name1,last_name=name2,password=pass1,email=email,username=phone,phone_code=phone_code,v_code=v_code,number=number,r_link=r_link,inviter_name=inviter_name,inviter_phone=inviter_phone)
                add.save()




                #send verification code

                
                import http.client


                #access token

                from urllib.request import urlopen
                import json
                conn = http.client.HTTPSConnection("auth.routee.net")

                payload = "grant_type=client_credentials"

                headers = {
                    'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                    'content-type': "application/x-www-form-urlencoded"
                    }

                conn.request("POST", "/oauth/token", payload, headers)

                res = conn.getresponse()
                data = res.read()


                data = data.decode("utf-8")

                json_obj = json.loads(data)

                access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                #send msg
                code = v_code

                phone = phone_code

                name = name1

                msg =   "Hello " + name + ", welcome to STOCK EXCHANGE. Your verification code is " + code

                conn = http.client.HTTPSConnection("connect.routee.net")

                payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                headers = {
                    'authorization': "Bearer "+access_token+"",
                    'content-type': "application/json"
                    }


                conn.request("POST", "/sms", payload, headers)


                res = conn.getresponse()
                data = res.read()


                
                
                username = request.POST["username"]
                password = request.POST["password1"]
                user =  authenticate(request,username=username, password=password)
                if user:

                    auth.login(request,user)


                    return redirect("v_code")


            
            

        else:
            messages.info(request, 'Passwords do not match', extra_tags='warning')
            return render(request , 'register.html' ,{'name' : name1,'name2':name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2})
    return render(request , "register.html")



import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

shortcode = "4048415"

passkey = "8a458b1f9bdcc40406e95eeb3f918c2e0268649d1214ecd0313e4770f761ca8b"

data_to_encode = shortcode + passkey+ formatted_time
encoded = base64.b64encode(data_to_encode.encode())

decoded_password = encoded.decode("utf-8")




consumer_key = "CFVSR5CF1UAr72jdAbBkcgfuUSL2YKZo"

consumer_secret = "fjUYspQyfY3JuYko"

api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

json_response = r.json()


my_access_token = json_response['access_token']


  
def deposit(request):
    if request.method == 'POST':
        phone  = request.user.detail.phone_code

        amount = request.POST['amount']

        access_token = my_access_token
        api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
        "BusinessShortCode": shortcode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": shortcode,
        "PhoneNumber": phone,
        "CallBackURL": "https://milanwriters.com/signup",
        "AccountReference": phone,
        "TransactionDesc": "pay"
        }

        response = requests.post(api_url, json = request, headers=headers)

        print(response.text)

        
        
        return redirect('dashboard2')
        





def withdraw(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            
            amount1 = request.POST['amount1']
            balance = int(request.user.detail.balance)
            phone = request.user.detail.phone
            phone_code = request.user.detail.phone_code
            name = request.user.first_name

            
           
            if amount1=="":
                messages.info(request, 'Invalid amount'  , extra_tags='warning')
                
                return redirect("dashboard")
            else:
                amount = int(request.POST['amount1'])
                if amount>balance:
                    
                    wit = str(amount)
                    messages.info(request, 'Insufficient balance to withdraw kes ' + wit , extra_tags='warning')
                    
                    return redirect("dashboard")

                else:
                
                    
                    if amount == 0 or amount<0:

                        
                        messages.info(request, 'Invalid amount'  , extra_tags='warning')
                    
                        return redirect("dashboard")
                    elif amount<300:

                        messages.info(request, 'Minimum withdrawal amount is kes 300'  , extra_tags='warning')
                    
                        return redirect('dashboard')

                    else:
                        bal = balance - amount




                        
                        import string
                        string.ascii_letters
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        import random
                        a =random.choice(string.ascii_letters)
                        a = a.upper()



                        import random

                        b = str(random.randint(10,99))

                        string.ascii_letters
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        import random
                        c =random.choice(string.ascii_letters)
                        c = c.upper()

                        d = str(random.randint(100,999))

                        


                       



                        #generate transaction code

                        

                        import string
                        string.ascii_letters
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        import random
                        a =random.choice(string.ascii_letters)
                        a1 = a.upper()



                        import random

                        b1 = str(random.randint(10,99))

                        string.ascii_letters
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        import random
                        c =random.choice(string.ascii_letters)
                        c1 = c.upper()

                        d1 = str(random.randint(100,999))

                        string.ascii_letters
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        import random
                        e =random.choice(string.ascii_letters)

                      


                        r_code = "W" +a1 + b1 + c1 +d1 



                
                        wit = str(amount)
                        num = str(phone)

                        balance = int(balance) - int(amount)

                        new = Withdrawal(amount=amount,phone=phone,balance=balance,name=name,ref=r_code)
                        new.save() 
                    
                        bal = balance - amount

                        phone = str(request.user.detail.phone)
                        c =  Detail.objects.get(phone=phone)
                        new2_save = Transaction(detail=c,amount=amount,t_type='Withdrew',phone=phone,ref=r_code)
                        new2_save.save()

                        Detail.objects.filter(phone=phone).update(balance=bal)









                        
                        import http.client


                        #access token

                        from urllib.request import urlopen
                        import json
                        conn = http.client.HTTPSConnection("auth.routee.net")

                        payload = "grant_type=client_credentials"

                        headers = {
                            'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                            'content-type': "application/x-www-form-urlencoded"
                            }

                        conn.request("POST", "/oauth/token", payload, headers)

                        res = conn.getresponse()
                        data = res.read()


                        data = data.decode("utf-8")

                        json_obj = json.loads(data)

                        access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                        #send msg
                       

                        phone = phone_code

                        

                        msg =   r_code + " Confirmed,you have withdrawn kes " + str(amount) + " to phone number " + str(num) + ".Your Stock Exchange account balance is kes " + str(bal)+ " .This will be processed in 5 minutes time.For any query call/sms 0740612197."

                        conn = http.client.HTTPSConnection("connect.routee.net")

                        payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                        headers = {
                            'authorization': "Bearer "+access_token+"",
                            'content-type': "application/json"
                            }


                        conn.request("POST", "/sms", payload, headers)


                        res = conn.getresponse()
                        data = res.read()


                


                        import http.client


                        #access token

                        from urllib.request import urlopen
                        import json
                        conn = http.client.HTTPSConnection("auth.routee.net")

                        payload = "grant_type=client_credentials"

                        headers = {
                            'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                            'content-type': "application/x-www-form-urlencoded"
                            }

                        conn.request("POST", "/oauth/token", payload, headers)

                        res = conn.getresponse()
                        data = res.read()


                        data = data.decode("utf-8")

                        json_obj = json.loads(data)

                        access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                        #send msg
                       

                        phone = str(254745685152)
                        bal1 = balance - amount



                        

                        msg =   name + " withdrew kes " + str(amount) + "  phone number " + str(num) + " balance is kes " + str(bal1)
                        conn = http.client.HTTPSConnection("connect.routee.net")

                        payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                        headers = {
                            'authorization': "Bearer "+access_token+"",
                            'content-type': "application/json"
                            }


                        conn.request("POST", "/sms", payload, headers)


                        res = conn.getresponse()
                        data = res.read()


                












                        messages.info(request, 'You have withdrawn kes ' + wit  + ' to mpesa number ' + num +'.' , extra_tags='success')
                        return redirect('dashboard')


                        
        else:
        
           
            return render(request, "withdraw.html" )
    
def buy_share(request):
    if request.user.is_authenticated:
        phone = request.user.detail.phone
        shares_status = request.user.detail.shares_status

        c =  Detail.objects.get(phone=phone)

        share =  Public_share.objects.get(name="none")
      

        x = c.verified

        balance = c.balance
        name = c.first_name

        
        available = int(share.remaining) * 10

        span = share.span

        if x ==True:
            if request.method== 'POST':
                amount = int(request.POST["b_amount"])
                period = int((request.POST["period"]))

                if amount>available:
                    messages.info(request, 'The requested amount of shares is more than the available shares.' , extra_tags='warning')
                    return redirect('dashboard')
                elif span == False:
                    messages.info(request, 'Sorry, todays trading session has already passed,please try again tommorow' , extra_tags='warning')
                    return redirect('dashboard')

                elif amount<2500:
                    messages.info(request, 'Minimum value of shares to buy is kes 2500' , extra_tags='warning')
                    return redirect('dashboard')
                elif balance<amount:
                    messages.info(request, 'Balance insufficient to buy shares worth kes ' + str(amount) , extra_tags='warning')
                    return redirect('dashboard')

                elif shares_status == True:

                    messages.info(request, 'You already have active shares,please wait for their maturity to buy others' , extra_tags='warning')
                    return redirect('dashboard')
                else:
                    bal = balance - amount

                    phone = str(request.user.detail.phone)
                    c =  Detail.objects.get(phone=phone)

                    phone_code2 = c.phone_code
                    new2_save = Transaction(detail=c,amount=amount,t_type='Bought Shares',phone=phone,ref=phone)
                    new2_save.save()

                    Detail.objects.filter(phone=phone).update(balance=bal)

                    shares = amount * 0.1

                    if period== 24:
                        payout = amount * 1.135

                        payout = round(payout)

                    elif period == 36:
                        payout = amount * 1.168
                        payout = round(payout)

                    else:
                        payout = amount * 1.197
                        payout = round(payout)

                    
                    code = Active_share.objects.last()
                    code = int(code.code)

                    code = code + 1

                    rem =  share.remaining - shares
                    bought =  share.bought + shares




                    
                    Public_share.objects.filter(name="none").update(bought=bought)

                    Public_share.objects.filter(name="none").update(remaining=rem)




                    new3_save = Active_share(detail=c,phone=phone,shares_amount=shares,shares_value=amount,profit=payout,period=period,name=name,code=code)
                    new3_save.save()

                    Detail.objects.filter(phone=phone).update(shares_status=True)

                    Detail.objects.filter(phone=phone).update(invest1=True)




                    
                    import http.client


                    #access token

                    from urllib.request import urlopen
                    import json
                    conn = http.client.HTTPSConnection("auth.routee.net")

                    payload = "grant_type=client_credentials"

                    headers = {
                        'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                        'content-type': "application/x-www-form-urlencoded"
                        }

                    conn.request("POST", "/oauth/token", payload, headers)

                    res = conn.getresponse()
                    data = res.read()


                    data = data.decode("utf-8")

                    json_obj = json.loads(data)

                    access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                    #send msg
                    code = v_code

                    detail1 =  Detail.objects.get(phone=phone)

                    bal22 = detail1.balance

                    
                    phone = phone_code2

                    

                    msg =   "Confirmed, You bought shares worth KES " +str(amount)+" from STOCK EXCHANGE.Payout after " +str(period)+" hours is KES " + str(payout) +". Your account balance is KES "  + str(bal22) + ". Thank you for trading with us."

                    conn = http.client.HTTPSConnection("connect.routee.net")

                    payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                    headers = {
                        'authorization': "Bearer "+access_token+"",
                        'content-type': "application/json"
                        }


                    conn.request("POST", "/sms", payload, headers)


                    res = conn.getresponse()
                    data = res.read()





                    messages.info(request, 'Confirmed,you bought shares worth ' + str(amount) + ".Payout after " + str(period) + " hours is kes " + str(payout) , extra_tags='success')



                    return redirect('dashboard')

        else:
            return redirect("v_code")


def previous(request):

    if request.user.is_authenticated:
        phone = request.user.detail.phone
        

        c =  Detail.objects.get(phone=phone)
        x = c.verified
        code = int(c.v_code)

        if x== False:
            return redirect("v_code")
            

        else:
            
            phone = request.user.detail.phone
            c =  Detail.objects.get(phone=phone)

            shares= c.active_share_set.all().order_by('-date')

            return render(request, 'previous.html' ,{'shares': shares})


def sell_share(request):

    if request.user.is_authenticated:
        phone = request.user.detail.phone
        name = request.user.detail.first_name
        

        c =  Detail.objects.get(phone=phone)
        x = c.verified
        code = int(c.v_code)

        if x== False:
            return redirect("v_code")
            

        else:
            
            phone = request.user.detail.phone
            c =  Detail.objects.get(phone=phone)


            shares= c.active_share_set.last()

            shares_value = shares.shares_value
            shares_amount = shares.shares_amount
            profit = shares.profit
            status = shares.status
            period = shares.period
            code = shares.code
      

            if request.method == 'POST':
                amount = int(request.POST["s_amount"])
                if status == True:
                    messages.info(request, 'You do not have active shares to sell.' , extra_tags='warning')
                    return redirect('dashboard')
                else:
                    if amount >shares_value:
                        messages.info(request, 'You shares value is less than kes ' + str(amount) , extra_tags='warning')
                        return redirect('dashboard')
                    if amount <2500:
                        messages.info(request, 'Minimum value of shares to sell is kes 2500' , extra_tags='warning')
                        return redirect('dashboard')

                    else:
                        Detail.objects.filter(phone=phone).update(shares_status=False)


                        Active_share.objects.filter(code=code).update(status=True)


             

                        new3_save = Sold_share(shares_amount=shares_amount,shares_value=shares_value,profit=profit,period=period,name=name,code=code,sale_amount=amount)
                        new3_save.save()

                        messages.info(request, 'You sold shares worth kes ' + str(amount) + " to stock exchange market, please wait as we approve." , extra_tags='success')
                        return redirect('dashboard')




def wallet(request):

    if request.method == 'POST':
        
        if request.user.is_authenticated:

            amount1 = str(request.POST['t_amount'])
            receiver = str(request.POST['phone'])
            sender = str(request.user.detail.phone)
            balance = int(request.user.detail.balance)

            phone = request.user.detail.phone
            c =  Detail.objects.get(phone=phone)

            
                

            if receiver =="":
                messages.info(request, 'Invalid phone'  , extra_tags='warning')
                return redirect('dashboard')

            elif amount1 =="":
                messages.info(request, 'Invalid amount'  , extra_tags='warning')
                return redirect('dashboard')

            elif amount1 == "0":
                messages.info(request, 'Invalid amount'  , extra_tags='warning')
                return redirect('dashboard')

            elif int(amount1) < 200:

                messages.info(request, 'Minimum amount to send is kes 200'  , extra_tags='warning')

                return redirect('dashboard')


            elif str(request.POST['phone'])== sender:
                messages.info(request, 'You can\'t send money to your own wallet'  , extra_tags='warning')
                return redirect('dashboard')

            else:
                
                if Detail.objects.filter(phone=receiver).exists():

                    amount = int(request.POST['t_amount'])
                    receiver = int(request.POST['phone'])
                    receiver1 = str(request.POST['phone'])
                    if balance<amount:            
                        messages.info(request, 'Your balance is less than '  + amount1 , extra_tags='warning')
                        return redirect('dashboard')

                    else:
                        
                        
                        new1 = Transfer(sender=sender,receiver=receiver,amount=amount)
                        new1.save()

                        bal = balance - amount

                        

                        Detail.objects.filter(phone=sender).update(balance=bal)
                        Detail.objects.filter(phone=receiver1).update(balance= F('balance') + amount)

                        phone = str(request.user.detail.phone)

                        c =  Detail.objects.get(phone=phone)
                        new2_save = Transaction(detail=c,amount=amount,t_type='Sent',phone=phone,ref=receiver)
                        new2_save.save()

                        x =  Detail.objects.get(phone=receiver1)
                        new3_save = Transaction(detail=x,amount=amount,t_type='Received',phone=phone,ref=phone)
                        new3_save.save()


                        amount = str(amount)
                        receiver = str(receiver1) 
                        messages.info(request, 'You have transferred kes ' +amount +' to  account '+ receiver  , extra_tags='success')
                        return redirect('dashboard')
                        


            
                else:
                    receiver = str(request.POST['phone'])
                    messages.info(request, 'Phone number ' + receiver +" do not have an account." , extra_tags='warning')
                    return redirect('dashboard')




def transaction(request):
    phone = request.user.detail.phone
    c =  Detail.objects.get(phone=phone)

    transactions= c.transaction_set.all().order_by('-date')



    return render(request, 'transactions.html' ,{'transactions': transactions})


def loans(request):
    messages.info(request, 'Failed, you are not eligible for a loan,please continue using our services to increase your loan limit', extra_tags='warning')
    

    return redirect('dashboard')




def change_password(request):
    if request.method == 'POST':
        username = request.user.username


        password2 = request.POST['password2']
        password3 = request.POST['password3']
        
        if password2 == password3:
            num= len(password2)
            if num<4:
                messages.info(request , 'Password should have more than 4 characters' , extra_tags='warning')
                return redirect('profile')
            else:
                u = User.objects.get(username=username)
                u.set_password(password2)
                u.save()
                user = auth.authenticate(username= username, password=password2)
                if user is not None:
                    auth.login(request , user)
                    
                    messages.info(request , 'Password Changed' , extra_tags='success')
                    return redirect('profile')
        else:
            messages.info(request , 'Password mismatch' , extra_tags='warning')
            return redirect('profile')


def i_list(request):

    phone = request.user.detail.phone
    c =  Detail.objects.get(phone=phone)

    promo= c.promotion_set.all().order_by('-date')



    return render(request, 'i_list.html' ,{'promo': promo})


def s_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        
        detail =  User.objects.get(username=username)
        none = detail.is_staff

        if none == False:
            messages.info(request , 'Access denied.', extra_tags='login')
            return redirect('s_login')
        else:
            user = auth.authenticate(username= username, password=password)
            if user is not None:
                auth.login(request , user)
                return redirect("staff_dashboard")
            
                
            else:
                
                messages.info(request , 'Invalid credentials', extra_tags='login')
                return redirect('s_login')

    else:
        
        return render(request, 's_login.html' )


def staff_dashboard(request):
    username  = request.user.username
    detail =  User.objects.get(username=username)
    none = detail.is_staff
    if none == False:
        messages.info(request , 'Access denied', extra_tags='login')
        return redirect('/')
    else:
        return render(request , "staff_dashboard.html")


def search_d(request):
    username  = request.user.username
    detail =  User.objects.get(username=username)
    none = detail.is_staff
    if none == False:
        messages.info(request , 'Access denied', extra_tags='login')
        return redirect('/')
    else:

        if request.method == 'POST':
            phone = request.POST['phone']
            if Detail.objects.filter(phone=phone).exists():

                user =  User.objects.get(username=phone)
                detail = Detail.objects.get(phone=phone)
                return render(request , 's_deposit.html',{'user':user ,'detail':detail})
            else:
                messages.info(request , 'User not available', extra_tags='not')
                return redirect("staff_dashboard")


        else:
            return render(request , 'staff.html')

def deposit22(request):
    username  = request.user.username
    detail =  User.objects.get(username=username)
    none = detail.is_staff
    if none == False:
        messages.info(request , 'Access denied', extra_tags='login')
        return redirect('/')
    else:      
        if request.method == 'POST':
            phone = request.POST['phone']
            detail =  Detail.objects.get(phone=phone)

            one = detail.invest1

            user =  User.objects.get(username=phone)
            balance = detail.balance
            
            inviter = detail.inviter_phone
            inviter_name = detail.inviter_name
            name = detail.first_name
           
           
            

            pay =  Detail.objects.get(phone=inviter)

            bal = pay.balance

            phone_code2 = detail.phone_code
            phone_code3 = pay.phone_code
            name2 = pay.first_name
            
           

            

            
            

            deposit2 = int(request.POST['deposit'])
            balance1 = int(request.POST['balance'])

            b1 = deposit2 + balance1

            
            paid = deposit2 * 0.1
            
            paid=(round(paid))
            paid_now = bal + paid

            


  
           

            if one==False:
                Detail.objects.filter(phone=inviter).update(balance=paid_now)
                
                Detail.objects.filter(phone=inviter).update(referal_income= F('referal_income') +paid)
                Detail.objects.filter(phone=inviter).update(total_income= F('total_income') +paid)


                


                Detail.objects.filter(phone=phone).update(balance=b1)
                c =  Detail.objects.get(phone=phone)
                new2_save = Transaction(detail=c,amount=deposit2,t_type='Deposited',phone=phone,ref=phone)
                new2_save.save()

                Detail.objects.filter(phone=phone).update(total_deposits= F('total_deposits') +deposit2)



                deposit2 = str(request.POST['deposit'])
                phone = str(request.POST['phone'])
                messages.info(request , 'You have deposited  KES ' + deposit2 + ' to ' + phone + ' inviter earned.',  extra_tags='depo')

                save33 = Deposit(phone=phone,inviter=inviter_name,amount=deposit2,inviter_earned=paid,name=name)



                save33.save()




                import http.client


                #access token

                from urllib.request import urlopen
                import json
                conn = http.client.HTTPSConnection("auth.routee.net")

                payload = "grant_type=client_credentials"

                headers = {
                    'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                    'content-type': "application/x-www-form-urlencoded"
                    }

                conn.request("POST", "/oauth/token", payload, headers)

                res = conn.getresponse()
                data = res.read()


                data = data.decode("utf-8")

                json_obj = json.loads(data)

                access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                #send msg
                code = v_code

                detail1 =  Detail.objects.get(phone=phone)

                bal22 = detail1.balance

                
                phone = phone_code2

                

                msg =   "Dear " +name+", You deposited KES " + str(deposit2) +" to STOCK EXCHANGE.Your account balance is KES "  + str(bal22) + ". Thank you for trading with us."

                conn = http.client.HTTPSConnection("connect.routee.net")

                payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                headers = {
                    'authorization': "Bearer "+access_token+"",
                    'content-type': "application/json"
                    }


                conn.request("POST", "/sms", payload, headers)


                res = conn.getresponse()
                data = res.read()


                #send msg
                code = v_code

                detail2 =  Detail.objects.get(phone=inviter)

                bal222 = detail2.balance

                
                phone1 = phone_code3

                

                msg =   "Dear " +name2+", You Earned KES " + str(paid) +" from a referral to  " +name +".Your balance is KES " + str(bal222) + ". Thank you for trading with STOCK EXCHANGE."

                conn = http.client.HTTPSConnection("connect.routee.net")

                payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone1+"\",\"from\": \"STOCKMAKERT\"}"



                headers = {
                    'authorization': "Bearer "+access_token+"",
                    'content-type': "application/json"
                    }


                conn.request("POST", "/sms", payload, headers)


                res = conn.getresponse()
                data = res.read()










                return redirect("staff_dashboard")

            else:
               


                Detail.objects.filter(phone=phone).update(balance=b1)
                c =  Detail.objects.get(phone=phone)
                new2_save = Transaction(detail=c,amount=deposit2,t_type='Deposited',phone=phone,ref=phone)
                new2_save.save()

                deposit2 = str(request.POST['deposit'])
                phone = str(request.POST['phone'])
                messages.info(request , 'You have deposited  ' + deposit2 + ' to ' + phone + ' inviter did not earn',  extra_tags='depo')
                save78 = Deposit(phone=phone,inviter=inviter_name,amount=deposit2,inviter_earned=paid)
                save78.save()


                import http.client


                #access token

                from urllib.request import urlopen
                import json
                conn = http.client.HTTPSConnection("auth.routee.net")

                payload = "grant_type=client_credentials"

                headers = {
                    'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                    'content-type': "application/x-www-form-urlencoded"
                    }

                conn.request("POST", "/oauth/token", payload, headers)

                res = conn.getresponse()
                data = res.read()


                data = data.decode("utf-8")

                json_obj = json.loads(data)

                access_token = (json_obj['access_token']) # prints the string with 'source_name' key




                #send msg
                code = v_code

                detail1 =  Detail.objects.get(phone=phone)

                bal22 = detail1.balance

                
                phone = phone_code2

                

                msg =   "Dear " +name+", You deposited KES " + str(deposit2) +" to STOCK EXCHANGE.Your account balance is KES "  + str(bal22) + ". Thank you for trading with us."

                conn = http.client.HTTPSConnection("connect.routee.net")

                payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



                headers = {
                    'authorization': "Bearer "+access_token+"",
                    'content-type': "application/json"
                    }


                conn.request("POST", "/sms", payload, headers)


                res = conn.getresponse()
                data = res.read()



                return redirect("staff_dashboard")

           
def refund(request):
    username  = request.user.username
    detail =  User.objects.get(username=username)
    none = detail.is_staff
    if none == False:
        messages.info(request , 'Access denied,staff only', extra_tags='login')
        return redirect('/')
    else:
    


        history= Active_share.objects.filter(status=False).order_by('date')


        return render(request, 'refund.html' ,{'history': history})


def pay_refund(request):
    username  = request.user.username
    detail =  User.objects.get(username=username)
    none = detail.is_staff
    if none == False:
        messages.info(request , 'Access denied,staff only', extra_tags='login')
        return redirect('/')
    else:
        if request.method == 'POST':
            phone = request.POST['mobile']
            pay = int(request.POST['pay'])
            code = request.POST['code']

            payment =  Active_share.objects.get(code=code)
            detail =  Detail.objects.get(phone=phone)

            balance = detail.balance
            status = payment.status
             
            new_balance = balance + pay

            Detail.objects.filter(phone=phone).update(balance=new_balance)
            Active_share.objects.filter(code=code).update(status=True)

            
            c =  Detail.objects.get(phone=phone)
            new2_save = Transaction(detail=c,amount=pay,t_type='Payout',phone=phone,ref=phone)
            new2_save.save()
            Detail.objects.filter(phone=phone).update(shares_status=False)

            pay = str(pay)
            phone = str(phone)

            Detail.objects.filter(phone=phone).update(total_income= F('total_income') +pay)
            Detail.objects.filter(phone=phone).update(shares_income= F('shares_income') +pay)
            


            messages.info(request , 'You have paid KES '  + pay + " to "+ phone, extra_tags='pay')



            import http.client


            #access token

            from urllib.request import urlopen
            import json
            conn = http.client.HTTPSConnection("auth.routee.net")

            payload = "grant_type=client_credentials"

            headers = {
                'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
                'content-type': "application/x-www-form-urlencoded"
                }

            conn.request("POST", "/oauth/token", payload, headers)

            res = conn.getresponse()
            data = res.read()


            data = data.decode("utf-8")

            json_obj = json.loads(data)

            access_token = (json_obj['access_token']) # prints the string with 'source_name' key




            #send msg
            code = v_code

            detail1 =  Detail.objects.get(phone=phone)

            bal22 = detail1.balance

            

            
            phone = detail1.phone_code

            

            msg =   "Dear Client, your shares worth KES " +str(pay)+" has matured and  deposited in your account .Account balance is KES " + str(bal22) + ". Thank you for trading with STOCK EXCHANGE."

            conn = http.client.HTTPSConnection("connect.routee.net")

            payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



            headers = {
                'authorization': "Bearer "+access_token+"",
                'content-type': "application/json"
                }


            conn.request("POST", "/sms", payload, headers)


            res = conn.getresponse()
            data = res.read()





            return redirect("refund")