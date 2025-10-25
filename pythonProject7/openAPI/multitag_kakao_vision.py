import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'b9ca7e6fcb8da3719636ca6542de8a8a'

def multi_tag(image_url):
    header = {'Authorization' : 'KakaoAK %s' % MYAPP_KEY}
    img_data = {'image_url' : image_url}
    response = requests.post(API_URL,
                             headers=header,
                             data=img_data)
    print(response)

    json_result = response.json()
    print(json_result)
    result = json_result['result']
    print(result)
    label_kr = result['label_kr']
    print(label_kr)


if __name__ == '__main__':
    multi_tag('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=sc960_832')