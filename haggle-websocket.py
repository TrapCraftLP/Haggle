import asyncio
import websockets
import json


class User:

    number_of_instances = 0

    def __init__(self, name, ip, key):
        self.id = User.number_of_instances
        User.number_of_instances += 1
        self.name = name
        self.ip = ip
        self.key = key


users = {}

def add_user(user_name, ip, key):
    users[user_name] = User(user_name, ip, key)    

async def hello(websocket, path):
    name = await websocket.recv()
    print("Test " + name)

    greeting = f"Hello {name} "

    await websocket.send(greeting)
    print(f"> {greeting}")

async def haggle(websocket, path):
    json_data = await websocket.recv()
    print(json_data)
    json_dict = json.loads(json_data)
    print(json_dict)
    if json_dict["command"] == "add":

        if json_dict["username"] is not None and json_dict["ip"] is not None and json_dict["key"] is not None:
            print("adding user")
            add_user(json_dict["username"], json_dict["ip"], json_dict["key"])
            await websocket.send("success")
    elif json_dict["command"] == "get":
        print("get")
        user = users[json_dict["username"]]
        print("user" + user.name)
        if user.key == json_dict["key"]:
            json_user = {"username": user.name, "ip":user.ip}
            await websocket.send(json.dumps(json_user))
    else:
        await websocket.send("error")

start_server = websockets.serve(haggle, port=9090)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
