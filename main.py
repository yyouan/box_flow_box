import websocket
from pi_camera import Scanner
import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json
import requests
from utils import genHash

cam = Scanner(0)

def button():
    a = input(" button: ")
    if a =="1":
        return True
    else:
        return False


#收到server傳來的message的callback
def onMessage(ws, msg):
    print("收到了從server傳來的message：" + msg)
    msg = json.loads(msg)
    

#與server建立連線後的callback
def onOpen(ws):
    sendMessage = '安安我是python'
    ws.send(sendMessage)

#server的HOST
HOST = 'ws://boxflow.herokuapp.com:12345'

#與server約定好的protocol server端也要設定
SUBPROTOCOLS = ['echo-protocol']

#建立websocket
ws = websocket.WebSocketApp(HOST, subprotocols = SUBPROTOCOLS, on_open = onOpen, on_message = onMessage)

#一直執行
ws.run_forever()

while True:
    if button():
        temp_name = genHash() + ".png"
        cam.get_photo(temp_name)
        with open(temp_name, "rb") as image:
            f = image.read()
            response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
            print(response_2.json())
            if len(response_2.json())!=0: 
                id_curr = response_2.json()[0]['faceId']
                print("id_curr:",id_curr)
                print(json.dumps(response_2.json()))
        msg = {"deposit":""}
        ws.send(json.dumps(msg))