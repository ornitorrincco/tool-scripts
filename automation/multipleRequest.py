import requests
import json
import time

HOSTService = ''
payload = {
    "text": "request 2"
}

while(True):
    time.sleep(1)
    try:
        response = requests.post(HOSTService, data=payload, timeout=1)
        print('Everything Fine')
    except:
        print('Timeout Error')
