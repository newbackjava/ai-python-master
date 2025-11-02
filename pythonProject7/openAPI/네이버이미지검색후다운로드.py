import os
import time
import requests

# 1) 네이버 발급값
CLIENT_ID = "8bCHy3sidsfXSMqXEXFtGWiEzQs"
CLIENT_SECRET = "nvsLFtGWiyNHMOG"

SEARCH_URL = "https://openapi.naver.com/v1/search/image"

query = "자동차"

headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET,
}

params = {
    "query": query,
    "display": 5,   # 몇 개 받을지
    "start": 1,
    "sort": "sim",
}

# 2) 이미지 검색 요청
resp = requests.get(SEARCH_URL, headers=headers, params=params, verify=False)

if resp.status_code != 200:
    print("search error:", resp.status_code, resp.text)
    raise SystemExit

data = resp.json()
items = data.get("items", [])

print(f"총 {len(items)}개 이미지 다운로드 시도...")

# 저장 폴더
save_dir = "downloads"
os.makedirs(save_dir, exist_ok=True)

# 3) 검색된 이미지들을 순서대로 다운로드
for idx, item in enumerate(items, start=1):
    img_url = item["link"]
    print(f"[{idx}] {img_url}")

    try:
        t0 = time.time()
        img_resp = requests.get(img_url, stream=True, timeout=10)
        img_resp.raise_for_status()

        # 확장자 대충 추출 (없으면 jpg)
        ext = os.path.splitext(img_url)[1]
        if not ext or len(ext) > 5:
            ext = ".jpg"

        filename = os.path.join(save_dir, f"{query}_{idx}{ext}")

        with open(filename, "wb") as f:
            for chunk in img_resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"  -> saved: {filename} ({time.time() - t0:.2f}s)")

    except Exception as e:
        print(f"  -> download failed: {e}")

print("끝!")
