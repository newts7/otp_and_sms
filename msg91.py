import requests
import json

def send_text_message(message,receiver):
    payload = {
        "sender" : "newts",
        "route" : "4",
        "country" : "91",
        "sms": [
            {
                "message": message,
                "to" : receiver
            }
        ]
    }
    print(payload)
    headers = {
        'authkey': "XXXXXXXXXXXXXXXXXXXXX",
        'content-type': "application/json"
        }
    response =  requests.post("http://api.msg91.com/api/v2/sendsms",data=json.dumps(payload),headers=headers)

    print(response)
send_text_message("Say hello to my friend",['81XXXXXX'])
