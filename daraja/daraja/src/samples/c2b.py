import requests
from requests.auth import HTTPBasicAuth

#access token

consumer_key = "Ow5fjyQNVshciJrAOvEZeE4d9GbfTJav"
consumer_secret = "Kb94FdD1ebsr7Leh"
api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"



r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']


#reg url
def register_url():

    api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
        "ShortCode": "4077967",
        "ResponseType": "Completed",
        "ConfirmationURL": "https://zidishajuniors.com/api/payments/c2b-confirmation/",
        "ValidationURL": "https://zidishajuniors.com/api/payments/c2b-validation/"}


   
    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

register_url()

def simulate_c2b_transaction():
   
  
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { 
        "ShortCode":"601521",
        "CommandID":"CustomerPayBillOnline",
        "Amount":"20",
        "Msisdn":"254708374149",
        "BillRefNumber":"456" }


    
    
    response = requests.post(api_url, json = request, headers=headers)

    
    print (response.text)

#simulate_c2b_transaction()
  
  