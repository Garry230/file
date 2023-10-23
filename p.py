
import requests,telebot
from telebot import types

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests,secrets,random,os
from user_agent import generate_user_agent


bot = telebot.TeleBot("5674469602:AAHkbsFsyY-8DgYBiOw4C6FD3DaTAAK0L9g")

@bot.message_handler(commands=['start'])
def start(message):
        global id
        id = message.from_user.id
        key = types.InlineKeyboardMarkup()
        key.row_width =2
        btn1=types.InlineKeyboardButton(text=f"- تعيين بروكسي .",callback_data="setProxy")
        btn2=types.InlineKeyboardButton(text=f"- انشاء حساب .",callback_data="create")
        btn3=types.InlineKeyboardButton(text=f"- Dev .",url="https://t.me/trprogram")
        key.add(btn1,btn2)
        key.add(btn3)
        bot.reply_to(message,f"- اهلا بك ايها القديم ..\n- اختر من الاسفل ..",reply_markup=key)
@bot.callback_query_handler(func=lambda call:True)
def ca(call):
    if call.data == "setProxy":
        bot.send_message(call.message.chat.id,f"None")
    if call.data == "create":
        crate_insta(call.message)
def setProxy(message):
    if ":" not in message.text or "." not in message.text:
        bot.reply_to(message,f"- تاكد من كتابه البروكسي بشكل صحيح ...")
    else:
        r.set(f"proxy-{id}",f"{message.text}")
        bot.reply_to(message,f"- {message.text} تم تعيينه بنجاح .")
def crate_insta(message):
	mm=bot.send_message(message.chat.id,f"[=] Type The Email ? ")
	bot.register_next_step_handler(mm,setEmail)
def setEmail(message):
	
	global Password,username,email,proxy,head_get_code,head,data_age,data_get_code,data_attemp,proxies,idd,Cookie
	email = message.text
	Cookie=secrets.token_hex(8)*8
	idd='X5uC6wALAAF-Lw3oSZE9kuY0mP_9'
	length=(int(9))
	chars="wwertyuiopasdfghjklzxcvbnmq_"
	for user in range(1):
		user=""
		for item in range(length):
			user+=random.choice(chars)
	for password in range(1):
		password=""
		for item in range(length):
			password+=random.choice(chars)
	username=str(user)
	Password=str(password)
	print("[/] Your Username is:",username)
	print("[\] Your Password is:",Password)
	with open('acc_iG_Un.txt', 'a') as x:
		inf=str(f"{email}:{Password}\tuser:{username}")
		x.write(inf+'\n')
		x.close
	head_get_code={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '67','content-type': 'application/x-www-form-urlencoded','cookie': Cookie,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(),'x-asbd-id': '437806','x-csrftoken': 'missing','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': 'missing',}
	head={'Host': 'www.instagram.com','Cookie': Cookie,'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': 'missing','X-Instagram-Ajax': 'missing','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k','Content-Type': 'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Content-Length': '432','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/accounts/emailsignup/','Te': 'trailers','Connection': 'close'}
	
	data_age={'day': '12','month': '1','year': '1996'}
	data_attemp={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{Password}','username': username,'first_name': 'BY @trprogram - @VV1CK','client_id': idd,'seamless_login_enabled': '1','opt_into_one_tap': 'false',}
	data_get_code={'device_id': "YwkwSAALAAFHoOfAgrw1j0-oJwKq",'email': email}
	try:
		req_attemp=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=head,data=data_attemp,verify=False)
		req_age=requests.post(f'https://www.instagram.com/web/consent/check_age_eligibility/',headers=head,data=data_age,verify=False)
		
		confirm_code(message)
	except requests.exceptions.ProxyError as rr:
		bot.reply_to(message,f"- قم بتغيير بروكسيك رجاءا ..")
		pass
def confirm_code(message):
    req_get_code=requests.post(f'https://i.instagram.com/api/v1/accounts/send_verify_email/',headers=head_get_code,data=data_get_code,verify=False)
    mm = bot.send_message(message.chat.id,f"- ارسل الكود الوصلك على ايميلك ..")
    bot.register_next_step_handler(mm,verify)
def verify(message):
    code = message.text
    data_send_code={'code': code,'device_id': "YwkwSAALAAFHoOfAgrw1j0-oJwKq",'email': email}
    req_send_code=requests.post(f'https://i.instagram.com/api/v1/accounts/check_confirmation_code/',headers=head_get_code,data=data_send_code,verify=False)
    try:singup_code=req_send_code.json()['signup_code']
    except:bot.reply_to(message,"[!!] Oops! You have a Error Check Your Info\n")
    try:data_crate={'email': email,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{Password}','username': username,'first_name': 'By @trprogram','month': '1','day': '12','year': '1996','client_id':"YwkwSAALAAFHoOfAgrw1j0-oJwKq",'seamless_login_enabled': '1','tos_version': 'row','force_sign_up_code': singup_code,}
    except:bot.reply_to(message,f"[!] Your code , {code} is Not Correct Please Check it And Try Again")
    req_crate=requests.post(f'https://www.instagram.com/accounts/web_create_ajax/',headers=head,data=data_crate,verify=False)
    try:
        if '"account_created": true' in req_crate.text:
            bot.reply_to(message,f'<strong>[+] Done Crate Account\n- Username : {username} .\n- Password : {Password}</strong>',parse_mode="html")
        elif "checkpoint_required" in req_crate.text:
            bot.reply_to(message,f'<strong>[+] Done Crate Account\n- Username : {username} .\n- Password : {Password}</strong>',parse_mode="html")
        elif "The IP address you are using has been flagged as an open proxy. If you believe this to be incorrect, please visit https://help.instagram.com/" in req_crate.text:
            bot.reply_to(message,"[!] IP Ban.")
            bot.reply_to(message,"[~] Retry With Another Email + VPN")
			#print(req_crate.text)
        elif "signup_block"==req_crate.json():
            bot.reply_to(message,"[!] IP Ban.")
            bot.reply_to(message,"[~] Retry With Another Email + VPN")
            #print(req_crate.text)
        elif "false"==req_crate.json()['account_created']:
            print(req_crate.json())
            bot.reply_to(message,"[~] Error in Crateing Account. ")
            bot.reply_to(message,"[-] Retry After A One Min ")
        else:bot.reply_to(message,f'<strong>[+] Done Crate Account\n- Username : {username} .\n- Password : {Password}</strong>',parse_mode="html")
    except:bot.reply_to(message,"[!!] Oops! You have a Error Check Your Info\n")
bot.infinity_polling()
