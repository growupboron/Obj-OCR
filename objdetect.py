import httplib, urllib, base64, json, re
from os import system

# CHANGE {MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = "3ce370692850429d98d3bfb773bc37c2"

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
conn.request("POST", "/vision/v1.0/analyze?%s"%params, body, headers)
response = conn.getresponse()
analysis = json.loads(response.read())
print(analysis)
print('hello')
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
response1 = conn.getresponse()
analysis1 = json.loads(response1.read())
print(analysis1)