import requests
from requests.auth import HTTPBasicAuth

#access token

consumer_key = "HO4TR7kYTt7VvGE7jGVzixSsZ476kGfM"
consumer_secret = "aPs2JRAf886lVNEj"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"



r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



json_response = r.json()

my_access_token = json_response['access_token']


#reg url
def register_url():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = {
        "ShortCode": "600584",
        "ResponseType": "Completed",
        "ConfirmationURL": "https://vinwamapp.herokuapp.com//c2b/confirmation",
        "ValidationURL": "https://vinwamapp.herokuapp.com//c2b/validation"}


   
    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

register_url()

def simulate_c2b_transaction():
   
  
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % my_access_token}
    request = { 
        "ShortCode":"600584",
        "CommandID":"CustomerPayBillOnline",
        "Amount":"20",
        "Msisdn":"254791848007",
        "BillRefNumber":"456" }


    
    
    response = requests.post(api_url, json = request, headers=headers)

    
    print (response.text)

#simulate_c2b_transaction()
  
  