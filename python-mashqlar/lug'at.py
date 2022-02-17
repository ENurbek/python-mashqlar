# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:47:57 2021

@author: 1
"""

asad={"ism":"asad", "tyil":"2005", "tsana":"7- May", "ish":"Programmist"}
ismi=asad["ism"]
tyili=asad["tyil"]
tsanasi=asad["tsana"]
ishi=asad["ish"]

abish={"ism":"abish", "tyil":"2006", "tsana":"10- May", "ish":"Programmist"}
a_ismi=abish["ism"]
a_tyili=abish["tyil"]
a_tsanasi=abish["tsana"]
a_ishi=abish["ish"]

nurik={"ism":"nurik", "tyil":"2007", "tsana":"11- May", "ish":"Programmist"}
n_ismi=nurik["ism"]
n_tyili=nurik["tyil"]
n_tsanasi=nurik["tsana"]
n_ishi=nurik["ish"]

print(f"Dustimning ismi {ismi.title()}, u {tyili}-{tsanasi}da Buxoroda tugulgan. U {ishi.upper()} bulib ishlaydi.")
print(f"Dustimning ismi {a_ismi.title()}, u {a_tyili}-{a_tsanasi}da Buxoroda tugulgan. U {a_ishi.upper()} bulib ishlaydi.")
print(f"Dustimning ismi {n_ismi.title()}, u {n_tyili}-{n_tsanasi}da Buxoroda tugulgan. U {n_ishi.upper()} bulib ishlaydi.")



python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

# .get() orqali 

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas!!!"))

# if va .get  orqali

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
   print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")