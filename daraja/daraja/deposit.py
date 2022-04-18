msg= "You received Ksh "+ str(50)+ " in your DIGITAL TRADE account.Your balance is Ksh" +str(30)





import http.client
phone = str(254112834819)

conn = http.client.HTTPSConnection("nzelej.api.infobip.com")
payload = "{\"messages\":[{\"from\":\"DIGITALTRADE\",\"destinations\":[{\"to\":"+phone+"}],\"text\":\"" +str(msg)+"\" }]}"
headers = {
    'Authorization': 'Basic RWR1aDI1NDpARWR3YXJkMjU0',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()