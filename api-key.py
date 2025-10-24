import requests

user_id = 123

# mock API. It's bad practice to expose an API key like that but this does nothing 
# and is only a tutorial on how API keys work
response = requests.request("GET", "https://api.mockapi.com/api/v1/user/{user_id}",
    headers={"x-api-key": "bd41b04c329chkjkj59f98454545"})

print(response.request.headers)

print(response.text)