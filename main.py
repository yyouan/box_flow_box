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




while True:
    print("no")
    if buttom.buttom():
        time.sleep(1)
        if buttom.buttom():
            print("long bottom")
            msg = {"withdraw": "","box_id":boxid}
            headers = {'Content-Type': 'application/json'}
            response_2 = requests.post("https://boxflow.herokuapp.com/withdraw", headers=headers, json = msg)
            print(response_2.content)
            #input("a")
            if response_2.content == b'OK':                
                servonew.turnquartercircle()
                while not buttom.buttom():
                    print("pass")
                    pass
                servonew.turnquartercircle()
                time.sleep(1)
                servonew.turnquartercircle()
                servonew.turnquartercircle()
                print(json.dumps(msg))
        else:            
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
                ans=""
                for resul in response_2.json()["recognitionResult"]["lines"]:
                    if len(json.dumps(resul["text"])) > 10:
                        ans = resul["text"]            
                servonew.turnonecircle()
                print("ID:",ans)
                print("rotate!")
                
                
            msg = {"deposit":ans ,"box_id":boxid}
            headers = {'Content-Type': 'application/json'} 
            response_2 = requests.post("https://boxflow.herokuapp.com/deposit", params=params, headers=headers, json = msg)
            print(json.dumps(msg))