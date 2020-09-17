# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri
import datetime
from random import randint

wiki = 'tr.wikipedia'
username='Mavrikant Bot'
xx = mavri.login(wiki, username)

one_day = datetime.timedelta(days=1)
baslangic = datetime.date(2015, 9, 1) # Bu tarihten öncesinde GM sorunlu. 
bugun = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
gelecekTarih = bugun + 2*one_day # 2 gün sonrası için kontrol yap
gelecekTarihStr = gelecekTarih.strftime("%Y-%m-%d")
kaynakTarih = baslangic + randint(0, int(str(bugun - baslangic).split(' days')[0])) * one_day # Başlangıç ve Bugün arasında rasgele bir tarih seç

logPage = 'User:'+username+'/Log/Günün Maddesi'

YarinSayfa = mavri.content_of_page(wiki, 'Şablon:GM/' + gelecekTarihStr)

if (YarinSayfa == ''):  # Yarının GM sayfası yok
    Summary = 'Olumsuz'
    Durum = '\n* {{Çapraz}}'

    # Kaynak sayfa bul ve içeriğini kopyala
    kaynakSayfa = mavri.content_of_page(wiki, 'Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d"))
    while kaynakSayfa == '':
        kaynakTarih += one_day # Sayfa boş çıktı. Sonraki güne geç.
        kaynakSayfa = mavri.content_of_page(wiki, 'Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d"))

    # Kaynak sayfa ile gelecek GM sayfasını oluştur
    mavri.change_page(wiki, 'Şablon:GM/' + gelecekTarihStr, kaynakSayfa, '[[Şablon:GM/' + kaynakTarih.strftime("%Y-%m-%d") + ']] sayfasından kopyalandı.', xx)

else:  # Yarının GM sayfası oluşturulmuş. Süper.
    Summary = 'Olumlu'
    Durum = '\n* {{Tamam}}'

# Log sayfasına rapor yaz
Durum += " [[Şablon:GM/%s | %s]]" %(gelecekTarihStr,gelecekTarihStr)
mavri.appendtext_on_page(wiki, logPage, Durum, Summary, xx)
