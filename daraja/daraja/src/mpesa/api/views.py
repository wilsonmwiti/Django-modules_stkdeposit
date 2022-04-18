
from rest_framework import serializers
from mpesa.models import LNMOnline



from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


from mpesa.models import LNMOnline,C2BPayments




class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = "id"


class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

     
    def create(self, request):
        print(request.data, "this is request.data")

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        print(merchant_request_id, "This should be MerchantReuestID")
        checkout_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        print(amount , "this should be an amount")
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        print(mpesa_receipt_number , "this should be receipt number")
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        print(transaction_date , "this should be transaction date")
        phone_number= request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        
        print(phone_number , "this should be phone number")
        from mpesa.models import LNMOnline
        
        
        exist = LNMOnline.objects.filter(MpesaReceiptNumber=mpesa_receipt_number).exists()
        
        if exist== True:
            print("already used")
            
        else:
                
        
            from datetime import datetime
    
            str_transaction_date = str(transaction_date)
    
            transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")
    
            from mpesa.models import LNMOnline
    
            our_model = LNMOnline.objects.create(
                CheckoutRequestID= checkout_request_id,
                MerchantRequestID = merchant_request_id,
                ResultCode = result_code,
                ResultDesc = result_description,
                MpesaReceiptNumber = mpesa_receipt_number,
                TransactionDate = transaction_datetime,
                PhoneNumber = phone_number,
                Amount = amount,
            )
    
            our_model.save()
            
            from rest_framework.response import Response
            
    
    
            return Response({"OurResultDesc":"YEEY!!! It worked"})
            
            
            
            

    
    

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = ("id","TransactionType","TransID","TransAmount","MSISDN","FirstName","MiddleName","LastName","BillRefNumber","BusinessShortCode")
        print("")

        
        

       
        
        
        

class C2BValidationAPIView(CreateAPIView):

    



    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

     
    def create(self, request):
    
       print(request.data, "this is request.data in validation")


    #    from rest_framework.response import Response


    #    return Response({"OurResultDesc":"YEEY!!! It worked"})

       

class C2BConfirmationAPIView(CreateAPIView):

    

    queryset = C2BPayments.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]
    
   
     
    def create(self, request):
    
    
    
         
        print(request.data, "this is request.data confirmation")
        
        TransID = request.data["TransID"]
        TransAmount = request.data["TransAmount"]
        BusinessShortCode = request.data["BusinessShortCode"]
        BillRefNumber = request.data["BillRefNumber"]
        MSISDN = request.data["MSISDN"]
        FirstName = request.data["FirstName"]
        MiddleName = request.data["MiddleName"]
        LastName = request.data["LastName"]
        OrgAccountBalance = request.data["OrgAccountBalance"]
        
        exist = C2BPayments.objects.filter(TransID=TransID).exists()
        
        if exist== True:
            print("already used")
            
        elif int(BusinessShortCode) != 4076921:
        
            print("Wrong Paybill")
                    
            
        else:
           
  
            our_model = C2BPayments.objects.create(
            
                    TransID= TransID,
                    TransAmount = TransAmount,
                    BusinessShortCode = BusinessShortCode,
                    BillRefNumber = BillRefNumber,
                    MSISDN = MSISDN,
                    FirstName = FirstName,
                    MiddleName = MiddleName,
                    LastName  = LastName ,
                    OrgAccountBalance=OrgAccountBalance,
                )
        
            our_model.save()
            
            
            
            
            
            
            from exchangeapp.models import Detail,Transaction,Deposit
            
           
            
            
            
            
            detail =  Detail.objects.get(phone=MSISDN)

           
            
            balance = detail.balance


            new_balance = float(TransAmount) + int(balance)
            
            inviter = detail.inviter_name

            
            name = detail.first_name
            email = detail.email


            Detail.objects.filter(phone=MSISDN).update(balance=new_balance)


            c =  Detail.objects.get(phone=MSISDN)

            new2_save = Deposit(amount=TransAmount,name=name,phone=MSISDN,inviter=inviter,balance=new_balance)
            new2_save.save()


            c =  Detail.objects.get(phone=MSISDN)

            t1_number = Transaction.objects.last()

            t1_number = int(t1_number.number)

            t1_number =t1_number + 1
            c =  Detail.objects.get(phone=MSISDN)
            new3_save = Transaction(detail=c,name=name,amount=TransAmount,t_type='Deposit',phone=MSISDN,number=t1_number)
            new3_save.save()
            
            
            
            
            
            first_name = request.data["FirstName"]
            print(first_name)
            
            phone =str(MSISDN)
            
    
        
    
            
            
            msg= "You received Ksh "+ str(TransAmount)+ " in your DIGITAL TRADE account.Your balance is Ksh" +str(new_balance)





            import http.client


            conn = http.client.HTTPSConnection("nzelej.api.infobip.com")
            payload = "{\"messages\":[{\"from\":\"DIGITALTRADE\",\"destinations\":[{\"to\":"+phone+"}],\"text\":\"" +str(msg)+"\" }]}"
            headers = {
                'Authorization': 'Basic RWR1aDI1NDpARWR3YXJkMjU0',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            conn.request("POST", "/sms/2/text/advanced", payload, headers)
            res = conn.getresponse()
            data = res.read()



            from django.core.mail import send_mail
            from django.conf import settings




            subject = 'DEPOSIT ,DIGITAL TRADE'
            message = msg
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )

    
            
            from rest_framework.response import Response
            
    
    
            return Response({"OurResultDesc":"YEEY!!! It worked"})
            



  






        
