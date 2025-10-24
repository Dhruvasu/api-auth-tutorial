import requests

user_id = 123

response = requests.request("GET", "https://api.mockapi.com/api/v1/user/{user_id}",
    headers={"x-api-key": "bd41b04c329chkjkj59f98454545"})

print(response.request.headers)

print(response.text)