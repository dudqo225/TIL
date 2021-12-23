import requests, json

URL = 'http://13.125.222.176/quiz/alpha'

data = {
    'nickname': '서울 4반 손영배',
    'yourAnswer': 'hellossafy',
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8',
}

res = requests.post(URL, headers=headers, data=json.dumps(data))

cnt = 1
while cnt < 20:
    if res.status_code == 200:
        cnt += 1
    
    dic = res.json()

    print(dic)
    
    nextURL = dic['nextUrl']
    req_url = f'http://13.125.222.176/quiz/{nextURL}'
    
    my_answer = input()
    ans = {
        'nickname': '서울 4반 손영배',
        'yourAnswer': my_answer,
    }

    res = requests.post(req_url, headers=headers, data=json.dumps(ans))