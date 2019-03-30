import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json
from utils import genHash
import requests
two_img ={
    "name": "box_flow_list",
    "userData": "User-provided data attached to the face list."
}

face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/facelists/boxflow'   

headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' }
    
params = {}

response = requests.put(face_api_url, params=params, headers=headers, json=two_img)

print(response)