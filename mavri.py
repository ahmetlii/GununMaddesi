# -*- coding: utf-8 -*-
# !/usr/bin/python

# mavri kütüphanesinin sadece gerekli olan fonksiyonları.
# Bu proje için kullanılmayanlar temizlendi.
# --Mavrikant

import json
import os
import re
import sys

import requests
import urllib.request

reload(sys)
sys.setdefaultencoding('UTF8')

def login(wiki, username):
    full_path = os.path.realpath(__file__)
    with open(os.path.dirname(full_path) + '/.pass') as data_file:
        data = json.load(data_file)
    passw = data[username]

    payload = {'action': 'query', 'format': 'json', 'utf8': '', 'meta': 'tokens', 'type': 'login'}
    r1 = requests.post('https://' + wiki + '.org/w/api.php', data=payload)

    login_token = r1.json()['query']['tokens']['logintoken']
    payload = {'action': 'clientlogin', 'format': 'json', 'utf8': '', 'username': username, 'password': passw,
               'logintoken': login_token}
    req = urllib.request.Request('https://' + wiki + '.org/w/api.php', data=payload, cookies=r1.cookies)
    with urllib.request.urlopen(req) as response:
        page_confirm = response.read()
            if (page_confirm = 'UI')
                urllib.request.Request('https://' + wiki + '.org/w/api.php?action=clientlogin&logincontinue=1&OATHToken=',"""bu kısma OATHToken gelmeli""", '&logintoken=', """buraya da normal token gelmeli""", cookies=r1.cookies)

def content_of_page(wiki, title):
    page= requests.get('https://' + wiki + '.org/w/index.php?title=' + title + '&action=raw')
    if ("<title>Wikimedia Error</title>" in page.text):
        return ""
    else:
        return page.text

def appendtext_on_page(wiki, title, appendtext, summary, xx):
    params3 = '?format=json&action=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    edit_token = r3.json()['tokens']['edittoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'appendtext': appendtext,
               'summary': summary,
               'title': title, 'token': edit_token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)

def change_page(wiki, title, text, summary, xx):
    params3 = '?format=json&action=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    edit_token = r3.json()['tokens']['edittoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'text': text,
               'summary': summary,
               'title': title, 'token': edit_token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)
