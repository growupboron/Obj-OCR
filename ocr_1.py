import httplib, urllib, base64, json, re
from os import system

# CHANGE {MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = ""

# setup vision API
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}

params = urllib.urlencode({
    'visualFeatures': 'Description',
})
print('hello')
body = open('1.jpeg', "rb").read()
conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
conn.request("POST", "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/")
response = conn.getresponse()
print(response)
analysis = json.loads(response.read())
print(analysis)
