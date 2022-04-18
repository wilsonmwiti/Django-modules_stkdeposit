import requests
from requests.auth import HTTPBasicAuth

#access token

consumer_key = "AIGd0cH6cqYjhDwgOPvfbuyHmwlpCGYh"
consumer_secret = "44Ds4DT2zzrfeZ9S"
api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


try:


    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

except:
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)


json_response = r.json()

my_access_token = json_response['access_token']



def register_url():

   

    api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": 4077965,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://profitarena.net/api/payments/c2b-confirmation/",
        "ValidationURL": "https://profitarena.net/api/payments/c2b-validation/"}
    

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


register_url()


def simulate_c2b_transaction():
    #my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        #"ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "4",
        #"Msisdn": keys.test_msisdn,
        "BillRefNumber": "myaccnumber",
    }
    try:
        response = requests.post(api_url, json=request, headers=headers)

    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


#simulate_c2b_transaction()