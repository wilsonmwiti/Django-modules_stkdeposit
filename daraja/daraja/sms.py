name= "EDWARD"
phone = str(254112834819)

code=str("horefho")
hello="hello"
msg= 'Hellonbyhuth' +  name





import http.client


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
print(data.decode("utf-8"))

