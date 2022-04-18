import requests

from requests.auth import HTTPBasicAuth


consumer_key = ""
consumer_secret = ""


api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']


#variables
shortcode = ""




username = ""

phone = 


amount = 100
  
def b2c_payment():

    
    access_token = my_access_token
    api_url = "https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "InitiatorName": username,
        "SecurityCredential":SecurityCredential,
        "CommandID": "SalaryPayment",
        "Amount": amount,
        "PartyA": shortcode,
        "PartyB": phone,
        "Remarks": "Thanks",
        "QueueTimeOutURL": "https://digitaltrade.tech/api/payments/B2cResultsess/",
        "ResultURL": "https://digitaltrade.tech/api/payments/B2cResults/",
        "Occasion": ""
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

    

b2c_payment()
    
    
    
 
