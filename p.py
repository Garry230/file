# import requests module
import requests
import time
import re
import secrets,random,os
from user_agent import generate_user_agent
# create a session object
s = requests.Session()

headers = {
    'authority': 'moakt.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__utmz=213295240.1693431232.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __gads=ID=5d9bd54b372f7831-22f9acb10de00098:T=1693431249:RT=1693773643:S=ALNI_MY_e2Q-O1iya2eRZH9Jrwl8M1tDTg; __gpi=UID=000009bbb4507ae1:T=1693431249:RT=1693773643:S=ALNI_MYExYMPLY5c4wVoVXg0H5RH9527VQ; __utma=213295240.491594152.1693431232.1693773642.1697918615.3; __utmc=213295240; __utmt=1; __utmb=213295240.1.10.1697918615',
    'origin': 'https://moakt.com',
    'referer': 'https://moakt.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}
length=(int(13))
chars="wwertyuiopasdfghjklzxcvbnmq123456789"
for user in range(1):
	user=""
	for item in range(length):
		user+=random.choice(chars)
yy=str(user)
data = {
    'domain': 'teml.net',
    'username': yy,
    'setemail': 'انشئ الآن',
    'preferred_domain': 'tmails.net',
}

response = s.post('https://moakt.com/ar/inbox', headers=headers, data=data)

print(response)
##
length=(int(11))
chars="wwertyuiopasdfghjklzxcvbnmq_"
for user in range(1):
	user=""
	for item in range(length):
		user+=random.choice(chars)
usernamee=str(user)
###
idd='X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
Cookie=secrets.token_hex(8)*8
head_get_code={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '67','content-type': 'application/x-www-form-urlencoded','cookie': Cookie,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(),'x-asbd-id': '437806','x-csrftoken': 'missing','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': 'missing',}
head={'Host': 'www.instagram.com','Cookie': Cookie,'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': 'missing','X-Instagram-Ajax': 'missing','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Content-Length': '432','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Te': 'trailers','Connection': 'close'}
data_attemp={'email': f'{yy}@teml.net','enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:Pp@ssw0rd!!','username': usernamee,'first_name': 'BY Nadji Moha 203','client_id': idd,'seamless_login_enabled': '1','opt_into_one_tap': 'false'}
data_age={'day': '12','month': '1','year': '1996'}
data_get_code={'device_id': "YwkwSAALAAFHoOfAgrw1j0-oJwKq",'email': f'{yy}@teml.net'}
req_attemp=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=head,data=data_attemp)
req_age=requests.post(f'https://www.instagram.com/web/consent/check_age_eligibility/',headers=head,data=data_age)
req_get_code=requests.post(f'https://i.instagram.com/api/v1/accounts/send_verify_email/',headers=head_get_code,data=data_get_code)
###
print(req_attemp)
print(req_age)
print(req_get_code)
##
while True:
    u=s.get('https://moakt.com/ar/inbox').text
    if 'instagram' in u:
        break
    else:
        pass
##

ee = s.get('https://moakt.com/ar/inbox')
eee = re.findall(r'href="/ar/email/(.*?)">(.*?) is your Instagram code', ee.text)
#print(eee[0][1])
codee=(eee[0][1])
#print(ee.text)


data_send_code={'code': codee,'device_id': "YwkwSAALAAFHoOfAgrw1j0-oJwKq",'email': f'{yy}@teml.net'}

req_send_code=requests.post(f'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',headers=head_get_code,data=data_send_code)
singup_code=req_send_code.json()['signup_code']

data_crate={'email': f'{yy}@teml.net','enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:Pp@ssw0rd!!','username': usernamee,'first_name': 'By Nadji Moha 203','month': '1','day': '12','year': '1996','client_id':"YwkwSAALAAFHoOfAgrw1j0-oJwKq",'seamless_login_enabled': '1','tos_version': 'row','force_sign_up_code': singup_code}

req_crate=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/',headers=head,data=data_crate)

print(req_crate)

if '"account_created": true' in req_crate.text:
    print(True)
    print(usernamee)
    print(f'{yy}@teml.net')
else:
    print(False)
