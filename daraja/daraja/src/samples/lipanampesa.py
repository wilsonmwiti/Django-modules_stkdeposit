import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

shortcode = "4077923"
passkey = "a56a2d903b6ee762cd48bfff1133b55b5a96abacb6c79615fdaf21d5437d3d22"

data_to_encode = shortcode + passkey+ formatted_time
encoded = base64.b64encode(data_to_encode.encode())

decoded_password = encoded.decode("utf-8")





consumer_key = "pU1pAN5lt3x65uPQDtGQFQXj6GrO4EEE"
consumer_secret = "2GAU6mxmGXJ9M4Uv"
api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']

phone = 254112834819

amount = 10


  
def lipa_na_mpesa():

    
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
    "CallBackURL": "https://larney.co.ke/api/payments/lnm/",
    "AccountReference": phone,
    "TransactionDesc": "pay"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print(response.text)

    print(response.CustomerMessage)



lipa_na_mpesa()
    

    



 
                   
    
    
 



        
