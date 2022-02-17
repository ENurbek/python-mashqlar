# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:15:26 2021

@author: 1
"""

lugat={
       "Book":"Kitob",
       "Pen":"Ruchka",
       "Mather":"Ona",
       "Father":"Ota",
       }
#print(lugat.keys())
#print(lugat.values())
for k, i in lugat.items():
    print(f"{k}- {i}")
 # print(i)
 
'''davlatlar={
           "Uzbekiston":"Toshkent",
           "Qozoqiston":"Ostona",
           "Turkmaniston":"Ashqabat",
           "Qirgiziston":"bishkek",
           "Afganistan":"qobul",
           }
print("Uzberiztonga qushni avlarlar:\n")
for davlat in sorted(davlatlar):
    print(f"{davlat.upper()}")

print("\nUzberiztonga qushni davlarlar poytaxtlari:\n")
for poytaxt in sorted(davlatlar.values()):
    print(f"{poytaxt.title()}")'''
    
    
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
