import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json

import requests

html = requests.get('https://i.imgur.com/L6vu1jV.jpg')
img_curr = html.content

img_name = 'a.jpg'
from PIL import Image
with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
	file.write(html.content)
	file.flush()
	file.close()

import os
cwd = os.getcwd()
im = Image.open(cwd+"\\a.jpg")
im_rotate = im.rotate(90)
im_rotate.save( "a1.jpg", quality=100 )
im_rotate = im.rotate(180)
im_rotate.save( "a2.jpg", quality=100 )
im_rotate = im.rotate(270)
im_rotate.save( "a3.jpg", quality=100 )

two_img ={
    "name": "box_flow_list",
    "userData": "User-provided data attached to the face list."
}

face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/facelists/boxflow/persistedFaces'   
params = {}
headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' ,
    'Content-Type': 'application/octet-stream'}

response_2 = requests.post(face_api_url, params=params, headers=headers, data = img_curr)
print(json.dumps(response_2.json()))

if not ("error" in response_2.json()): 
    id_curr = response_2.json()['persistedFaceId']
    print("id_curr:",id_curr)   
    
with open("a1.jpg", "rb") as image:
    f = image.read()
    response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
    print(response_2.json())
    if not ("error" in response_2.json()): 
        id_curr = response_2.json()['persistedFaceId']
        print("id_curr:",id_curr)
        print(json.dumps(response_2.json()))
with open("a2.jpg", "rb") as image:
    f = image.read()
    response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
    print(response_2.json())
    if not ("error" in response_2.json()): 
        id_curr = response_2.json()['persistedFaceId']
        print("id_curr:",id_curr)
        print(json.dumps(response_2.json()))
with open("a3.jpg", "rb") as image:
    f = image.read()
    response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
    print(response_2.json())
    if not ("error" in response_2.json()): 
        id_curr = response_2.json()['persistedFaceId']
        print("id_curr:",id_curr)
        print(json.dumps(response_2.json()))
