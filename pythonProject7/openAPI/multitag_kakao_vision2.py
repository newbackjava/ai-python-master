import sys
import argparse
from collections import Counter
from tkinter import messagebox

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'b9ca7e6fcb8da3719636ca6542de8a8a'

def multi_tag(image_url):
    # files = {'image': open("car1.gif", 'rb')}
    header = {'Authorization' : 'KakaoAK %s' % MYAPP_KEY
              }
    img_data = {'image_url' : image_url}
    response = requests.post(API_URL,
                             headers=header,
                             data=img_data)
    # print(response)

    json_result = response.json()
    #print(json_result)
    result = json_result['result']
    #print(result)
    label_kr = result['label_kr']
    print(label_kr)
    return label_kr #리스트
    # ['사람', '여러사람', '여성', '남성', '바지']
    # ['사람', '여러사람', '여성', '남성', '안경', '바지']
    # ['사람', '여러사람', '스포츠', '실외', '여성', '남성', '바지', '모자']

if __name__ == '__main__':
    img_list = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F396%2F2021%2F08%2F01%2F0000588233_001_20210801173212646.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130307_122%2Flee_hong1_1362641107335AqRvr_JPEG%2F1%25B9%25DA.jpg&type=sc960_832'
                ]
    result_list = []
    for img in img_list:
        label_result = multi_tag(img)
        result_list += label_result
    print(result_list)

    # from collections import Counter
    count_result = Counter(result_list)
    print(count_result)
    # Counter({'사람': 3, '여러사람': 3, '여성': 3, '남성': 3, '바지': 3, '안경': 1, '스포츠': 1, '실외': 1, '모자': 1})
    print(count_result.get('안경'))
    # 1
    print(count_result.most_common(1))
    # [('사람', 3)]
    print(count_result.most_common(5))
    # [('사람', 3), ('여러사람', 3), ('여성', 3), ('남성', 3), ('바지', 3)]
    order_5 = count_result.most_common(5)
    print(order_5[0]) #('사람', 3)
    order_1 = order_5[0]
    print('제일 빈도수가 높은 단어는 ', order_1[0],
          '이고, 빈도수는 ', order_1[1]
          )
    # 제일 빈도수가 높은 단어는 사람 이고, 빈도수는 3

    tour = ''
    if order_1[0] == '사람':
        tour = '제주도'
    elif order_1[0] == '남성':
        tour = '등산'
    else:
        tour = '놀이공원'
    messagebox.showinfo('추천', '당신에게 ' +
                        tour +
                        '를 추천합니다.' )

    #result.txt
    #사람,제주도



