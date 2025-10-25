

import requests
from PIL import Image

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'b9ca7e6fcb8da3719636ca6542de8a8a'

def multi_tag(img):
    file = {'image': open(img, 'rb')}
    header = {'Authorization' : 'KakaoAK %s' % MYAPP_KEY}
    response = requests.post(API_URL,
                             headers=header,
                             files=file)
    # print(response)

    json_result = response.json()
    print(json_result)

if __name__ == '__main__':
    label_result = multi_tag('alone.png')
    print(label_result)

