########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json
from pi_camera import Scanner
cam = Scanner(0)
import requests
#html = requests.get('https://i.imgur.com/cywHUYb.jpg')
#img_curr = html.content
from utils import genHash

temp_name = genHash() + ".png"
cam.get_photo(temp_name)

with open(temp_name, "rb") as image:    
    
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': '',
    })

    try:
        face_api_url = 'https://eastasia.api.cognitive.microsoft.com/vision/v2.0/ocr'        

        headers = { 'Ocp-Apim-Subscription-Key': '889e3520642847629a48a7849e8de5e8'  ,
    'Content-Type': 'application/octet-stream'}
            
        params = {
            'language': 'unk',
            'detectOrientation': 'true',
        }
        response_2 = requests.post(face_api_url, params=params, headers=headers, data = image)        
        print(json.dumps(response_2.json()))

    except Exception as e:
        print(e)

    


####################################
    
