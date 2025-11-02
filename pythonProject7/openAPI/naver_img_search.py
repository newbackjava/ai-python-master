import requests
import json

# 네이버 발급값으로 바꾸세요
CLIENT_ID = "8bCHy3MqXEXFtGWewewsdiEzQs"
CLIENT_SECRET = "nvsLyNDFSEHMOG"

url = "https://openapi.naver.com/v1/search/image"

# 검색어
query = "코드랩"

headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
}

params = {
    "query": query,
    "display": 5,   # 가져올 개수
    "start": 1,
    "sort": "sim",  # sim: 유사도순, date: 날짜순
}

resp = requests.get(url, headers=headers, params=params, verify=False)

if resp.status_code == 200:
    data = resp.json()
    # 이미지 링크만 뽑아서 보기
    for item in data.get("items", []):
        print(item["link"])
else:
    print("error:", resp.status_code, resp.text)
