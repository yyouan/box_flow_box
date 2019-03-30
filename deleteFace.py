import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json

import requests
two_img ={}

face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/facelists/boxflow/persistedFaces/c1912bfa-fffb-4616-8159-38f7756da2dc'   

headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' }
    
params = {}

response = requests.delete(face_api_url, params=params, headers=headers, json=two_img)

print(response)