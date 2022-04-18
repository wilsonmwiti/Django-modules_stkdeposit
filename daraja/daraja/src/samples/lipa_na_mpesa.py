import requests
import base64
import keys
# import datetime

from requests.auth import HTTPBasicAuth

# print(datetime.datetime.now())
from datetime import datetime

unformatted= datetime.now()
formatted =unformatted.strftime("%Y%m%d%H%M%S")
# print(formatted)


# data_to_encode = formatted + keys.Business_shortCode + keys.Lipa_na_Mpesa_Passkey
# encoded= base64.b64encode(data_to_encode.encode())

# print(encoded)

# decoded =encoded.decode('utf-8')


# print(decoded)

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret

api_URL = (
    "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
)
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print(r.json)

json_response= r.json()
my_access_token = json_response['access_token']

def lip_na_mpesa():
    access_token = my_access_token
    api_url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers ={"Authorization":"Bearer %s" % access_token}
    request ={
        "BusinessShortCode":keys.Business_shortCode,    
        "Password": keys.password,    
        "Timestamp":formatted,    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount":"1",    
        "PartyA":600584,    
        "PartyB":keys.Business_shortCode,    
        "PhoneNumber":keys.Phone,    
        "CallBackURL":"https://mydomain.com/pat",    
        "AccountReference":"123456789",    
        "TransactionDesc":"Test"
    }
    response=requests.post(api_url,json=request,headers=headers)
    print(response.text)
lip_na_mpesa()