import requests

cookies = {
    'NNB': 'TQWKSEPKGLRV6',
    'ASID': 'dc76f81d0000017692b3945f0000004f',
    'recent_card_list': '10315,10112,10056,4044,10361,10359,10113',
    '_ga_8P4PY65YZ2': 'GS1.1.1727101753.4.1.1727101753.60.0.0',
    '_ga': 'GA1.2.311771527.1725895665',
    '_ga_0ZGH3YC3W6': 'GS1.2.1733668811.4.0.1733668811.0.0.0',
    '_fbp': 'fb.1.1738506959634.815589832377500396',
    'tooltipDisplayed': 'true',
    'NFS': '2',
    'NaverSuggestUse': 'unuse%26use',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    '_fwb': '29OSOZaPYxMOMDZpnbemXf.1744028282749',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '29OSOZaPYxMOMDZpnbemXf.1744028282749',
    'NAC': 'xqOOBQQ0G69Z',
    'nhn.realestate.article.trade_type_cd': '""',
    'SHOW_FIN_BADGE': 'Y',
    'NACT': '1',
    'SRT30': '1745320596',
    'realestate.beta.lastclick.cortar': '1162000000',
    'SRT5': '1745322681',
    'REALESTATE': 'Tue%20Apr%2022%202025%2020%3A54%3A27%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'Njq3AacBVrxrGwm2jE9O9Z4JG9DhNTj7K5nJHk-rk6o=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDUzMjI4NjcsImV4cCI6MTc0NTMzMzY2N30.XohUwDKjH_x3HXmf7-u-nePznxROcCk_Zu9-ti8dtPM',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/112392?ms=37.2046018,127.0498168,16&a=PRE:ABYG:JGC:APT&e=RETAIL',
    'sec-ch-ua': '"Chromium";v="134", "Whale";v="4", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Whale/4.31.304.16 Safari/537.36',
    # 'cookie': 'NNB=TQWKSEPKGLRV6; ASID=dc76f81d0000017692b3945f0000004f; recent_card_list=10315,10112,10056,4044,10361,10359,10113; _ga_8P4PY65YZ2=GS1.1.1727101753.4.1.1727101753.60.0.0; _ga=GA1.2.311771527.1725895665; _ga_0ZGH3YC3W6=GS1.2.1733668811.4.0.1733668811.0.0.0; _fbp=fb.1.1738506959634.815589832377500396; tooltipDisplayed=true; NFS=2; NaverSuggestUse=unuse%26use; nhn.realestate.article.rlet_type_cd=A01; _fwb=29OSOZaPYxMOMDZpnbemXf.1744028282749; landHomeFlashUseYn=Y; _fwb=29OSOZaPYxMOMDZpnbemXf.1744028282749; NAC=xqOOBQQ0G69Z; nhn.realestate.article.trade_type_cd=""; SHOW_FIN_BADGE=Y; NACT=1; SRT30=1745320596; realestate.beta.lastclick.cortar=1162000000; SRT5=1745322681; REALESTATE=Tue%20Apr%2022%202025%2020%3A54%3A27%20GMT%2B0900%20(Korean%20Standard%20Time); BUC=Njq3AacBVrxrGwm2jE9O9Z4JG9DhNTj7K5nJHk-rk6o=',
}

response = requests.get(
    'https://new.land.naver.com/api/articles/complex/112392?realEstateType=PRE%3AABYG%3AJGC%3AAPT&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=3&complexNo=112392&buildingNos=&areaNos=&type=list&order=rank',
    cookies=cookies,
    headers=headers,
)

print(response.text)

import json

# JSON 데이터를 파일로 저장
with open('naver_land_data.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)


