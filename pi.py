import picamera, httplib, urllib, base64, json, re
from os import system
from picamera import PiCamera
from time import sleep

# CHANGE {MS_API_KEY} BELOW WITH YOUR MICROSOFT VISION API KEY
ms_api_key = "{MS_API_KEY}"

# camera button - this is the BCM number, not the pin number
camera_button = Button(27)

# setup camera
camera = picamera.PiCamera()

# setup vision API
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ms_api_key,
}

params = urllib.urlencode({
    'visualFeatures': 'Description',
})

# loop forever waiting for button press
while True:
    camera_button.wait_for_press()
    camera.capture('/tmp/image.jpg')

    body = open('/tmp/image.jpg', "rb").read()

    try:
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

        conn.close()

    except Exception as e:
        print e.args
