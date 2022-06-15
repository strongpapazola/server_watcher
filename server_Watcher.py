data = [
{
    "ip" : "103.41.207.167",
    "name" : "ai-creation.bisaai.id"
},
]

import requests
import icmplib
import json

url = "https://discordapp.com/api/webhooks/986536654196047893/xvzWA3jyvFfHlAHWpIOtHZ3LbOdshQDmyff8qxPYHu0CpDWCbXb2QZK1S"

# use icmp for ping server
while True:
    for i in data:
        alive = icmplib.ping(i['ip'])
        if alive.is_alive == True:
            print(f"{i['name']} : {alive.is_alive}")
        else:
            print(f"{i['name']} : {alive.is_alive}")
            response = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=json.dumps({"content": f"> :red_circle: {i['name']} Was Dead Waiting to be Alive"}))
            print(response.text)
            while True:
                alive = icmplib.ping(i['ip'])
                print(f"waiting server {i['name']} alive", end='\r')
                if alive.is_alive == True:
                    response = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=json.dumps({"content": f"> :green_circle: {i['name']} Was Alive"}))
                    print(response.text)
                    print(f"{i['name']} : {alive.is_alive}")
                    break


    

