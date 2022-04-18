import requests
from requests.auth import HTTPBasicAuth

def generate_access_token():

    consumer_key = "x4r4ZSpDmZ6oFxrSr4EEgNeknyu0xHy5"
    consumer_secret = "QINABL90BdDR7uqJ"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



    json_response = r.json()

    my_access_token = json_response['access_token']

    return my_access_token