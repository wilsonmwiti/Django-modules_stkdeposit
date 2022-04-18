import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#print(formatted_time)

shortcode = "174379"
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

data_to_encode = shortcode + passkey+ formatted_time
encoded = base64.b64encode(data_to_encode.encode())

decoded_password = encoded.decode("utf-8")




consumer_key = "x4r4ZSpDmZ6oFxrSr4EEgNeknyu0xHy5"
consumer_secret = "QINABL90BdDR7uqJ"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']

phone = 254745685152

amount = 15
  
def lipa_na_mpesa():


    
    access_token = my_access_token

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "BusinessShortCode": shortcode ,
            "Password": decoded_password,
            "Timestamp": formatted_time,
            "CheckoutRequestID": " "
        }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

    lipa_na_mpesa()
    
    
    
    
 import requests
  
  
  



        
