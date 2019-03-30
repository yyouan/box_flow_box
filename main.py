import websocket
from pi_camera import Scanner
import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json
import requests
from utils import genHash
import time
import servonew
import buttom
from PIL import Image

cam = Scanner(0)
boxid = "box1"

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
#ws.run_forever()

while True:
    print("no")
    if buttom.buttom():
        print("button on!")
        temp_name = genHash() + ".png"
        print("camera on!")
        cam.get_photo(temp_name)
        im = Image.open(temp_name)
        im_rotate = im.rotate(180)
        im_rotate.save( temp_name, quality=100 )
        with open(temp_name, "rb") as image:    
            '''
            headers = {
                # Request headers
                'Content-Type': 'application/json',
                'Ocp-Apim-Subscription-Key': '6ac893d0038b433a8f993c52ea6b300b',
            }
            '''
            face_api_url = 'https://eastasia.api.cognitive.microsoft.com/vision/v2.0/recognizeText'        
            
            headers = { 'Ocp-Apim-Subscription-Key': '6ac893d0038b433a8f993c52ea6b300b'  ,
            'Content-Type': 'application/octet-stream'}
                
            params = urllib.parse.urlencode({
                'mode': 'Printed'
            })
            url={"url":"https://i.imgur.com/TKYGb6p.jpg"}
            #response_2 = requests.post(face_api_url, params=params, headers=headers, json=url) 
            response_2 = requests.post(face_api_url, params=params, headers=headers, data = image)        
            print(response_2.headers["Operation-Location"])
            headers = {
                # Request headers
                'Ocp-Apim-Subscription-Key': '6ac893d0038b433a8f993c52ea6b300b',
            }
            time.sleep(3) 
            response_2 = requests.get(response_2.headers["Operation-Location"], headers=headers)    
            #print(json.dumps(response_2.json()))
            
            for resul in response_2.json()["recognitionResult"]["lines"]:
                if len(json.dumps(resul["text"])) > 10:
                    ans = resul["text"]
            print("ID:",ans)
            print("rotate!")
            servonew.turnonecircle()
            
            
        msg = {"deposit":ans ,"box_id":boxid}
        ws.send(json.dumps(msg))
        print(json.dumps(msg))