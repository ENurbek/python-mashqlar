# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:59:59 2021

@author: 1
"""
buyurtma=[]
n=1
print("Buyurtmalarni qabul qilamiz".upper()) 

while True:
    buyurt=input(f"{n}- Buyurtmani kiriting? ")
    buyurtma.append(buyurt)
   # n+=1
    savol=input("Yana buyurtma kiritasizmi? (Y/N, Yes/No, Ha/Yuq)>>")
    n+=1
    if savol=="N" or savol=="No" or savol=="Yuq":
       break 

'''print("\nBuyurtmalar ro\'yxati\n".upper())
#print(buyurtma)
s=len(buyurtma)    
for a in range(s):
    print(buyurtma[a])'''
    
    
Eco_bozor={}
d=1
print("\nEco bozor".upper())
while True:
   mahsulot=input(f"{d}- Mahsulot nomini kiriting? ")
   narh=float(input(f"{mahsulot.title()}ni narxini kiriting? "))
   Eco_bozor[mahsulot]=narh
   savol=input("Yana buyurtma kiritasizmi? (Y/N, Yes/No, Ha/Yuq)>>")
   d+=1
   if savol=="N" or savol=="No" or savol=="Yuq":
       break 
'''print("\nEco bozordagi mahsulotlar va narxlari. \n")   
for mahsulot, narx in Eco_bozor.items():
    print(f"{mahsulot.title()}- {narx} so\'m")'''
    
    
'''s=len(buyurtma)    
for a in range(s):
    if buyurtma[a] in Eco_bozor[mahsulot]:
        print(buyurtma[a], Eco_bozor=narx)'''



while buyurtma:
    buyurt = buyurtma.pop()
    if buyurt in Eco_bozor.keys():
        sena = Eco_bozor[buyurt]
        print(f"{buyurt.title()} - {sena} so'm")
    else:
        print(f"Bizda {buyurt.title()} yo'q")        