import requests
###send code
eem = input('Entre  email here :: ')
headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '2.625',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/email/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-G955U"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'viewport-width': '412',
    'x-asbd-id': '129477',
    'x-csrftoken': 'EcyRUi6ji3Lkfu0qj3KXIM8EQVZtxL7c',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1009412997',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'EAE071D0-150D-4368-A8C4-DC134949368A',
}

data = {
    'device_id': 'ZTbLDgALAAH7SUmd2nKj9swfopbx',
    'email': eem,
}

response = requests.post(
    'https://www.instagram.com/api/v1/accounts/send_verify_email/',
    headers=headers,
    data=data,
)

print(response.text)

###entre code
ee = input('Entre code here :: ')

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ig_did=EAE071D0-150D-4368-A8C4-DC134949368A; datr=Dcs2ZWQ-qDSfdWFW0Eeh2zjr; csrftoken=EcyRUi6ji3Lkfu0qj3KXIM8EQVZtxL7c; mid=ZTbLDgALAAH7SUmd2nKj9swfopbx; ig_nrcb=1',
    'dpr': '2.625',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/emailConfirmation/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-G955U"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'viewport-width': '412',
    'x-asbd-id': '129477',
    'x-csrftoken': 'EcyRUi6ji3Lkfu0qj3KXIM8EQVZtxL7c',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1009412997',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'EAE071D0-150D-4368-A8C4-DC134949368A',
}

data = {
    'code': ee,
    'device_id': 'ZTbLDgALAAH7SUmd2nKj9swfopbx',
    'email': eem,
}

responseo = requests.post(
    'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
    headers=headers,
    data=data,
)

print(responseo.text)
## set name
'''
headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '2.625',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/birthday/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-G955U"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'viewport-width': '412',
    'x-asbd-id': '129477',
    'x-csrftoken': 'EcyRUi6ji3Lkfu0qj3KXIM8EQVZtxL7c',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1009412997',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'EAE071D0-150D-4368-A8C4-DC134949368A',
}

data = {
    'email': eem,
    'name': 'by Nadji',
}

response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
    headers=headers,
    data=data,
)

print(response.text)
'''
## confirm finally # set passwd and user

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '2.625',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/signup/username/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-G955U"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'viewport-width': '412',
    'x-asbd-id': '129477',
    'x-csrftoken': 'EcyRUi6ji3Lkfu0qj3KXIM8EQVZtxL7c',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1009412997',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'EAE071D0-150D-4368-A8C4-DC134949368A',
}
sn = responseo.json()["signup_code"]
data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1698089972:P@ssw0rd!',
    'day': '23',
    'email': eem,
    'first_name': 'by nadji',
    'month': '10',
    'username': eem.split('@')[0],
    'year': '2002',
    'client_id': 'ZTbLDgALAAH7SUmd2nKj9swfopbx',
    'seamless_login_enabled': '1',
    'tos_version': 'row',
    'force_sign_up_code': sn,
}

response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
    headers=headers,
    data=data,
)

print(response.text)
