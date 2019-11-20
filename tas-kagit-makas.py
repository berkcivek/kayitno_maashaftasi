#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:39:37 2019

@author: berk
"""
import time
import random

print('Merhaba! Taş-Kağıt-Makas oyununa hoşgeldiniz!\n')
secim = input('Lütfen Bir Seçim Yapınız  - Taş , Kağıt yada Makas:\t').strip().capitalize()

tas="""'
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'"""

makas="""'
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'"""

kagit="""'
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'"""

if secim == 'Makas':
    print('Kullanıcı Seçimi:\n' + makas)
    time.sleep(1)
    tmp = random.randint(1,3)
    #1= Makas,2=Taş,3=Kağıt
    if tmp==1:
        sonuc = makas + '\n Raund Berabere!'
    elif tmp ==2:
        sonuc = tas +'\n Bilgisayar Kazandı!'
    else:
        sonuc = kagit + '\n Kullanıcı Kazandı!'        
    print(sonuc)        
elif secim == 'Taş':
    print('Kullanıcı Seçimi:\n' + tas)
    time.sleep(1)
    tmp = random.randint(1,3)
    if tmp==1:
        sonuc = makas +'\n Kullanıcı Kazandı!'
    elif tmp ==2:
        sonuc = tas + '\n Raund Berabere!'
    else:
        sonuc = kagit +'\n Bilgisayar Kazandı!'        
    print(sonuc)   
elif secim == 'Kağıt':
    print('Kullanıcı Seçimi:\n' + kagit)
    time.sleep(1)
    tmp = random.randint(1,3)
    if tmp==1:
        sonuc = makas + '\n Bilgisayar Kazandı!'
    elif tmp ==2:
        sonuc = tas + '\n Kullanıcı Kazandı!'
    else:
        sonuc = kagit + '\n Raund Berabere!'      
    print(sonuc)       
else:
    print('Hatalı Giriş,Tekrar deneyiniz')
