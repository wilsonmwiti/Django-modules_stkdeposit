import http.client


        #access token

from urllib.request import urlopen
import json
conn = http.client.HTTPSConnection("auth.routee.net")

payload = "grant_type=client_credentials"

headers = {
    'authorization': "Basic NWZlYjIzZmNhNmVkODgwMDAxODExZWY4OnJwTmRTamN0em4=",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()


data = data.decode("utf-8")

json_obj = json.loads(data)

access_token = (json_obj['access_token']) # prints the string with 'source_name' key




#send msg
code ="Code"


bal22 ="bal"


phone = str(254791848007)

name = "Edward"

msg =   "Dear " +name+", You deposited KES " + str(60) +" to STOCK EXCHANGE.Your account balance is KES "  + str(bal22) + ". Thank you for trading with us."

conn = http.client.HTTPSConnection("connect.routee.net")

payload = "{ \"body\": \""+msg+"\",\"to\" : \""+phone+"\",\"from\": \"STOCKMAKERT\"}"



headers = {
    'authorization': "Bearer "+access_token+"",
    'content-type': "application/json"
    }


conn.request("POST", "/sms", payload, headers)


res = conn.getresponse()
data = res.read()
print(res)