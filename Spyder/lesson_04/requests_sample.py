import json
import requests

from PIL import Image
from io import BytesIO

# print(dir(requests))

'''
url = 'http://www.baidu.com'
r = requests.get(url)
print(r.text)
print(r.status_code)
print(r.encoding)
'''

# 传递参数：不如http://aaa.com?pageId=1&type=content
'''
params = {'k1':'v1', 'k2':'v2'}
r = requests.get('http://httpbin.org/get', params)
print(r.url)
'''

# 二进制数据
'''
r = requests.get('http://i-2.shouji56.com/2015/2/11/23dab5c5-336d-4686-9713-ec44d21958e3.jpg')
image = Image.open(BytesIO(r.content))
image.save('meinv.jpg')
'''

# json处理
'''
r = requests.get('https://github.com/timeline.json')
print(type(r.json))
print(r.text)
'''

# 原始数据处理
'''
r = requests.get('http://i-2.shouji56.com/2015/2/11/23dab5c5-336d-4686-9713-ec44d21958e3.jpg', stream = True)
with open('meinv2.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
'''

# 提交表单
'''
form = {'username':'user', 'password':'pass'}
r = requests.post('http://httpbin.org/post', data = form)
print(r.text)
r = requests.post('http://httpbin.org/post', data = json.dumps(form))
print(r.text)
'''

# cookie
'''
url = 'http://www.baidu.com'
r = requests.get(url)
cookies = r.cookies
for k, v in cookies.get_dict().items():
    print(k, v)
'''
'''
cookies = {'c1':'v1', 'c2': 'v2'}
r = requests.get('http://httpbin.org/cookies', cookies = cookies)
print(r.text)
'''

# 重定向和重定向历史
'''
r = requests.head('http://github.com', allow_redirects = True)
print(r.url)
print(r.status_code)
print(r.history)
'''

# 代理
'''
proxies = {'http': ',,,', 'https': '...'}
r = requests.get('...', proxies = proxies)
'''
    

