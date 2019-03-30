import requests
html = requests.get('https://i.imgur.com/guB31A7.jpg')
img_name = 'a.png'
with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
	file.write(html.content)
	file.flush()
	file.close()