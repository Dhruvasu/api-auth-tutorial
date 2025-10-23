import requests
import base64

username = "user"
password = "pwd"

# combine into single bytes-like object
credentials = f'{username}:{password}'.encode('utf-8')

# encode into Base64
encoded_creds = base64.b64encode(credentials).decode('utf-8')

print("Base64 encoded creds: " + encoded_creds)

url = 'https://httpbin.org/basic-auth/my_username/my_password'

response = requests.get(url, auth=(username, password))
print(response.status_code)

auth_header = response.request.headers.get('Authorization')
print('Authorization header set: ' + auth_header)

if response.status_code == 200:
    print("Authorization successful")
    print('Response JSON:' + response.json())
else:
    print("Authorization unsuccessful")
    print('Response JSON:' + response.json())