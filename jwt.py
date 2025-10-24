import requests
import urllib3
import jwt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cml_url = "https://cml.nwl.lab/api"
cml_username = "admin"
cml_password = "Cisco123"

auth_payload = {
    "username": cml_username,
    "password": cml_password
}

auth_headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json'
}

auth_token = requests.post(f"{cml_url}/v0/authenticate", 
                         headers=auth_headers, 
                         json=auth_payload, 
                         verify=False).json()

print("Encoded JWT token")
print(auth_token)

labs_headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {auth_token}'
}

labs = requests.get(f"{cml_url}/v0/labs", 
                   headers=labs_headers, 
                   verify=False).json()

print(f"Found {len(labs)} labs:")

for lab_id in labs:
    lab_details = requests.get(f"{cml_url}/v0/labs/{lab_id}", 
                             headers=labs_headers, 
                             verify=False).json()
    print(f"Title: {lab_details['lab_title']}")
    print(f"State: {lab_details['state']}")
    print(f"Created: {lab_details['created']}")
    print(f"URL: {cml_url.replace('/api', '')}/lab/{lab_id}")
    print("-" * 80)