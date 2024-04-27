
import requests as re

def get_method ():
    url = "https://reqres.in/api/users?page=2"

    resp = re.get(url)
    if resp.status_code == 200:
        respnce_date = resp.json()
        print("success", respnce_date)
    else:
        print("failed")
res = get_method()
print(res)


def post_methos():
    url = "https://reqres.in/api/register"
    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    resp = re.post(url, json=data)
    
    if resp.status_code == 200:
        resp_data = resp.json()
        status = resp.status_code
        print(status)
        print("responce", resp_data)
    else:
        print("failed to register")

b = post_methos()
print(b)
