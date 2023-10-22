import requests
ee = input("Entre Email : ")
headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '2',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/email/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi 8A"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '360',
    'x-asbd-id': '129477',
    'x-csrftoken': 'FR1rFaW5eu0QNySyioHANTJftCNRCBRl',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR1muDEkGKbbLJj-9MYWyLYtwVTVtTJEtHOlsjRT9eoXoQFt',
    'x-instagram-ajax': '1009405475',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'device_id': 'ZN4xRgABAAG6MaaNg4DwXDY4iZTg',
    'email': ee,
}

response = requests.post(
    'https://www.instagram.com/api/v1/accounts/send_verify_email/',
    headers=headers,
    data=data,
)

print(response.text)
