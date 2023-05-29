import requests

url = 'https://46.101.199.136:8090/login'

data = {
    'username': 'myusername',
    'password': 'mypassword'
}

client_cert = 'client1.crt'

client_key = 'client1.key'

response = requests.post(url, data=data, verify='server.crt', cert=(client_cert, client_key))

print(response.text)
