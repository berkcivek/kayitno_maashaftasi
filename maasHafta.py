#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:33:53 2019

@author: Berk Osman Civek & Asım Burak Gündüz
"""
tc=input('Lütfen kayıt numaranızı giriniz:\t').replace(' ','')
tcl=len(tc)
if tcl == 11:
    orta= tc[int(tcl/2)]
    orta_no=int(orta)
    if orta_no <= 5:
        if orta_no %2 == 0:
            hafta = 'Ayın ilk haftası'
        else:
            hafta= 'Ayın ikinci haftası'
    else:
        if orta_no %2 == 0:
            hafta= 'Ayın üçüncü haftası'
        else:
            hafta= 'Ayın son haftası'        
    print('Maaş haftanız:\t'+hafta)
else:
    print('Kayıt numaranız 11 haneden oluşmak zorunda!')



