#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:59:36 2019

@author: berk
"""
print('Merhaba,Şifre oluşturma programına hoşgeldiniz.Lütfen şifre oluşturmak için gerekli adımları takip edin.')

zorluk=input('Şifreniz nasıl olsun? - (1)Kolay (2)Orta (3)Zor - Numarasını tuşlayın:\t').strip()

if zorluk == '1':
    kelime= input('Şifrenizde kullanılacak bir kelime giriniz:\t').strip()
    numara= input('Şifrenizde kullanılacak bir numara giriniz:\t').strip()
    sifre= kelime+numara
    print(sifre)
elif zorluk == '2':
    kelime= input('Şifrenizde kullanılacak bir kelime giriniz:\t').strip()
    numara= input('Şifrenizde kullanılacak bir numara giriniz:\t').strip()
    if len(numara)>=5:
        sifre= numara[0:3]+kelime+numara[3:]
    elif len(numara) < 5 and len(numara)>=2:
        sifre= numara[0:2]+kelime+numara[2:]
    else:
        sifre= kelime[int(len(kelime)/2)]+numara+kelime[int(len(kelime)/2)+1:]
    print(sifre)
elif zorluk == '3':
    ozel_karakter= input('Şifrenizde kullanmak istediğiniz özel karakter varsa tuşlayın yoksa geçin:\t')
    kelime= input('Şifrenizde kullanılacak bir kelime giriniz:\t').strip()
    numara= input('Şifrenizde kullanılacak bir numara giriniz:\t').strip()
    if len(ozel_karakter) >=1:
        if len(numara)>=5:
            sifre= numara[0:2]+kelime+numara[2:4]+ozel_karakter+kelime+numara[4:]
        elif len(numara) < 5 and len(numara)>=2:
            sifre= numara[0]+ozel_karakter+numara[1]+kelime+numara[2:]
        else:
            sifre= kelime[int(len(kelime)/2)-1]+ozel_karakter+kelime[int(len(kelime)/2)]+numara+kelime[int(len(kelime)/2)+1:]      
    else:
        if len(numara)>=5:
            sifre= numara[0:2]+kelime+numara[2:4]+kelime+numara[4:]
        elif len(numara) < 5 and len(numara)>=2:
            sifre= numara[0]+numara[1]+kelime+numara[2:]
        else:
            sifre= kelime[int(len(kelime)/2)-1]+kelime[int(len(kelime)/2)]+numara+kelime[int(len(kelime)/2)+1:]
    print(sifre)        
else:
    print('Hatalı giriş yaptınız,lütfen tekrar giriniz!')
