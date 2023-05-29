import requests

url = 'https://46.101.199.136:8090/login'

data = {
    'username': 'myusername',
    'password': 'mypassword'
}

response = requests.post(url, data=data, verify='server.crt')

print(response.text)
