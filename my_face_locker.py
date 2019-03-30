########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,requests,json

import requests
html = requests.get('https://i.imgur.com/cywHUYb.jpg')
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
    face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/detect'

    image_url = 'https://i.imgur.com/L6vu1jV.jpg'

    headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' }
        
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': '',
    }

    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    id_url = response.json()[0]['faceId']
    print(json.dumps(response.json()))

    headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' ,
    'Content-Type': 'application/octet-stream'}
    response_2 = requests.post(face_api_url, params=params, headers=headers, data = img_curr)
    
    if len(response_2.json())!=0: 
        id_curr = response_2.json()[0]['faceId']
        print("id_curr:",id_curr)
        print(json.dumps(response_2.json()))
    
    with open("a1.jpg", "rb") as image:
        f = image.read()
        response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
        print(response_2.json())
        if len(response_2.json())!=0: 
            id_curr = response_2.json()[0]['faceId']
            print("id_curr:",id_curr)
            print(json.dumps(response_2.json()))
    with open("a2.jpg", "rb") as image:
        f = image.read()
        response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
        print(response_2.json())
        if len(response_2.json())!=0: 
            id_curr = response_2.json()[0]['faceId']
            print("id_curr:",id_curr)
            print(json.dumps(response_2.json()))
    with open("a3.jpg", "rb") as image:
        f = image.read()
        response_2 = requests.post(face_api_url, params=params, headers=headers, data = f)
        print(response_2.json())
        if len(response_2.json())!=0: 
            id_curr = response_2.json()[0]['faceId']
            print("id_curr:",id_curr)
            print(json.dumps(response_2.json()))
#verify

    two_img ={
        "faceId1": id_url,
        "faceId2": id_curr,
    }

    face_api_url = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/verify'   

    headers = { 'Ocp-Apim-Subscription-Key': '057353660709425d8f69277c2297dee3' }
        
    params = {}

    response = requests.post(face_api_url, params=params, headers=headers, json=two_img)

    print(json.dumps(response.json()))

except Exception as e:
    print(e)

####################################