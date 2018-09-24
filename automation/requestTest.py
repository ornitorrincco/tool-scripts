import requests, time
r = requests.post('https://requestb.in/1flp59v1', data={"key1":"hola mundo"})
print(r.status_code)
print(r.content)
