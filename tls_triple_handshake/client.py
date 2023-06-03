import requests
import time

url = 'https://46.101.199.136:8090/login'

data = {
    'username': 'myusername',
    'password': 'mypassword'
}

while True:
    response = requests.post(url, data=data, verify='server.crt')

    print(response.text)

    time.sleep(60)
