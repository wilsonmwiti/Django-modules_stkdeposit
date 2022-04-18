import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime
from requests import Response



class MpesaResponse(Response):
	response_description = ""
	error_code = None
	error_message = ''

class MpesaConnectionError(Exception):
	"""
	Raised when connection has an error
	"""
	pass


def mpesa_response(r):
	"""
	Create MpesaResponse object from requests.Response object
	
	Arguments:
		r (requests.Response) -- The response to convert
	"""

	r.__class__ = MpesaResponse
	json_response = r.json()
	r.response_description = json_response.get('ResponseDescription', '')
	r.error_code = json_response.get('errorCode')
	r.error_message = json_response.get('errorMessage', '')
	return r


def stk_push():

    #access token

    consumer_key = "4ZE74XaUH0mbtRDXpkDGamfEOa5vnVGa"
    consumer_secret = "hk7IYwr0L0EBPWgw"
    api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



    json_response = r.json()

    mpesa_access_token = json_response['access_token']



    phone_number = 254112834819

    amount=15
    url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"


    passkey = "1f6a3ee947b2e4bd44c64135427b1acfcf577ea1172d34969a0ba005903b396e"
    
 

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    business_short_code = str(4076921)

    password = base64.b64encode((business_short_code + passkey + timestamp).encode('ascii')).decode('utf-8') 
    transaction_type = 'CustomerPayBillOnline'
    party_a = phone_number
    party_b = business_short_code

    callback_url = "https://larney.co.ke/api/payments/lnm/"
    transaction_desc = "payment"
    account_reference = "1234"

    data = {
        'BusinessShortCode': business_short_code,
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': transaction_type,
        'Amount': amount,
        'PartyA': party_a,
        'PartyB': party_b,
        'PhoneNumber': phone_number,
        'CallBackURL': callback_url,
        'AccountReference': account_reference,
        'TransactionDesc': transaction_desc
    }

    headers = {
        'Authorization': 'Bearer ' + mpesa_access_token,
        'Content-type': 'application/json'
    }

    try:

        r = requests.post(url, json=data, headers=headers)
        response = mpesa_response(r)
        print(response.text)
        return response

    except requests.exceptions.ConnectionError:
        raise MpesaConnectionError('Connection failed')
    except Exception as ex:
        raise MpesaConnectionError(str(ex))


#stk_push()






def b2c_payment():

    #access token

    consumer_key = "5kC8vAJ0AQAhGVEeTgvAVxEzFgTe79po"
    consumer_secret = "raAFb0XAdkSIQYV8"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))



    json_response = r.json()

    mpesa_access_token = json_response['access_token']
		

	

    phone_number = 254708374149
    
    url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"

    business_short_code = 600979
    

    party_a = business_short_code
    party_b = phone_number

    initiator_username = "testapi"
    initiator_security_credential = "V9FFg2Puc7O0eIDmxKLHoZTsAb5EAJeast8vZLZy2n/y0qeMxFH3O7lw7BL07bW2pJEIYpXo6dBgkgA8jxIbbt1VEa93YomtJSG6RYL3igo7XMqCqkWnYbQrzO45sIJJdwbzzf/EhEyVr4sJTYvDmj464a62flAB+vz3q7k3RUP49jBY2kvMwMzj5zFpIEVuxIptlGZdBMld2xI/tPeQWeRulOC0Zkh/5Qq4wMDhQotEvdsq68BRJdNwMNjDmxFNXvGE7/tScqSm/EVybtSNoWWd2KpJWoJil4Sqhld3eza7NXUZqb56sgIXn+8qDR4524AtxZu6HJvfY0mTHhVtyg=="
    

    data = {
        'InitiatorName': initiator_username,
        'SecurityCredential': initiator_security_credential,
        'CommandID': "BusinessPayment",
        'Amount': "20",
        'PartyA': party_a,
        'PartyB': party_b,
        'Remarks': "payment made",
        'QueueTimeOutURL': "https://darajambili.herokuapp.com/b2c/result",
        'ResultURL': "https://darajambili.herokuapp.com/b2c/result",
        'Occassion':  "payment"
    }

    headers = {
        'Authorization': 'Bearer ' + mpesa_access_token,
        'Content-type': 'application/json'
    }

    try:
        r = requests.post(url, json=data, headers=headers)
        response = mpesa_response(r)
        print(response.text)
        return response
    except requests.exceptions.ConnectionError:
        raise MpesaConnectionError('Connection failed')
    except Exception as ex:
        raise MpesaConnectionError(str(ex))


b2c_payment()               






    
