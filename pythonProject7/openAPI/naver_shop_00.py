import requests
import json

# 네이버에서 발급받은 값으로 바꾸세요
CLIENT_ID = "8bCHy3MqXEXFtGWewewsdiEzQs"
CLIENT_SECRET = "nvsLyNDFSEHMOG"


url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/age"

# 보낼 데이터
payload = {
    "startDate": "2025-08-01",
    "endDate": "2025-09-30",
    "timeUnit": "month",
    "category": "50000000",      # 패션의류
    "keyword": "바람막이",
    "device": "",
    "gender": "",
    "ages": ["10", "20", "30", "40", "50"]
}

headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
    "Content-Type": "application/json",
}

# mac에서 인증서 문제 있으면 verify=False 임시로 추가
resp = requests.post(url, headers=headers, json=payload, verify=False)

# 상태코드 확인
print("status:", resp.status_code)

# 응답 JSON 보기 좋게
if resp.status_code == 200:
    data = resp.json()  # dict 로 바로
    print(json.dumps(data, ensure_ascii=False, indent=2))
else:
    print("error:", resp.text)
