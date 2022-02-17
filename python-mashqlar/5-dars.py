# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:46:46 2021

@author: 1
"""

ism_sharif = 'james bond'
print(ism_sharif.title())


ism_sharif = 'james bond'       #James Bond
print(ism_sharif.capitalize())  #James bond
print('james bond'.upper())     #JAMES BOND


meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")#Men olma      yaxshi ko'raman
print("Men " + meva.rstrip() + " yaxshi ko'raman")#Men      olma yaxshi ko'raman
print("Men " + meva.strip() + " yaxshi ko'raman")#Men olma yaxshi ko'raman
print("Men " + meva + " yaxshi ko'raman")#Men      olma      yaxshi ko'raman


#ism = input("Ismingiz nima?")
#print("Assalom alaykum, " + ism)


#ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
#print("Assalom alaykum, " + ism.title())





kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")   

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())