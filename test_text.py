########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json
import time
from PIL import Image
from pi_camera import Scanner
cam = Scanner(0)
import requests
#html = requests.get('https://i.imgur.com/cywHUYb.jpg')
#img_curr = html.content
from utils import genHash

temp_name = genHash() + ".png"
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
    print(ans)
    


####################################
    
