import requests
#r = requests.get('https://www.google.com.tw/')
r = requests.get('http://127.0.0.1:5000/magic')
print(r.status_code)
print(r.text)