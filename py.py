import requests,secrets
###send code
from user_agent import generate_user_agent
Cookie=secrets.token_hex(8)*8
Userr=generate_user_agent()
email=input('Entre Email here : ')
username=input('Entre username : ')
headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': Userr,
    'viewport-width': '748',
    'x-asbd-id': '129477',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'missing',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'E33071EE-3C24-400B-9ED6-CFB25CBD80F6',
}

data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1698080303:AVJQACISNR2OUXKwM5hZoJv7PywairYhZ3iGZF66nCLCz1BdKi9CUl8layCKCkRUmtWrIUDfjNFTzKia1cdWDPoE+VWB77JD3vyGXLOOA7U1fvu7EDkGSbvDh+QlhE9noR5hbUQFo//a5L9w3rQiqw==',
    'email': email,
    'first_name': 'by nadji',
    'username': username,
    'client_id': 'ZTalvgALAAFfy6KqsmBjF5R-vDxH',
    'seamless_login_enabled': '1',
    'opt_into_one_tap': 'false',
}

response = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
    headers=headers,
    data=data,
)

print(response.text)

####

headers3 = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': Userr,
    'viewport-width': '748',
    'x-asbd-id': '129477',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'missing',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'E33071EE-3C24-400B-9ED6-CFB25CBD80F6',
}

data3 = {
    'day': '23',
    'month': '10',
    'year': '2000',
}

response3 = requests.post(
    'https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',
    headers=headers3,
    data=data3,
)

print(response3.text)

####
headers5 = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': Userr,
    'viewport-width': '748',
    'x-asbd-id': '129477',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'missing',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'E33071EE-3C24-400B-9ED6-CFB25CBD80F6',
}

data5 = {
    'device_id': 'ZTalvgALAAFfy6KqsmBjF5R-vDxH',
    'email': email,
}

response5 = requests.post(
    'https://www.instagram.com/api/v1/accounts/send_verify_email/',
    headers=headers5,
    data=data5,
)
print(response5.text)

####
code=input('Entre code : ')
headers6 = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': Userr,
    'viewport-width': '748',
    'x-asbd-id': '129477',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'missing',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'E33071EE-3C24-400B-9ED6-CFB25CBD80F6',
}

data6 = {
    'code': code,
    'device_id': 'ZTalvgALAAFfy6KqsmBjF5R-vDxH',
    'email': email,
}

response6 = requests.post(
    'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
    headers=headers6,
    data=data6,
)
sn = response6.json()["signup_code"]
print(response6.text)
####
headers77 = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': Cookie,
    'dpr': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.71", "Google Chrome";v="118.0.5993.71", "Not=A?Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': Userr,
    'viewport-width': '748',
    'x-asbd-id': '129477',
    'x-csrftoken': 'missing',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'missing',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': 'E33071EE-3C24-400B-9ED6-CFB25CBD80F6',
}

data77 = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1698080389:AVJQAPDRAKV/h6Qj5ysCjlHAd8ui2UGSktRvwseMpauRftx6hXMGhEXYWoCJ25Y+FV06c9xX1DNtuHpFnLJZ/zG7118zWjj85dkn2DZT3i74BCjOW2XWUUU0mXreuI/5VJJh5s25IbUDeVBZV+TGHw==',
    'day': '23',
    'email': email,
    'first_name': 'by nadji',
    'month': '10',
    'username': username,
    'year': '2000',
    'client_id': 'ZTalvgALAAFfy6KqsmBjF5R-vDxH',
    'seamless_login_enabled': '1',
    'tos_version': 'row',
    'force_sign_up_code': sn,
}

response77 = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
    headers=headers77,
    data=data77,
)

print(response77.text)
