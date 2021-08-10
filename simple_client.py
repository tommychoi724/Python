import requests
#r = requests.get('https://www.google.com.tw/')
sum=0

r = requests.get('http://192.168.0.136:5000/magic')
#print(r.text)
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.142:5000/magic')
#print(r.text)
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.141:5000/magic')
#print(r.text)
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.140:5000/magic')
#print(r.text)
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

r = requests.get('http://192.168.0.134:5000/magic')
#print(r.text)
m = r.json()
print (m[0]["result"])
sum += m[0]["result"]

print(sum)