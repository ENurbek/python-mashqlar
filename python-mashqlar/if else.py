# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:36:19 2021

@author: 1
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for a in cars:
    if a=="gm":
      print("GM")
    else:
        print(a.title())
        
        
'''l=input("Loginingizni kiriting? \n >>>")
if len(l)<5:
    print("Login 5 ta xarfdan uzun bo\'lsin!!!")
elif l=="Admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
     print(f"Xush kelibsiz, {l}!" )'''
     
     
'''son=int(input("Son kiriting? "))
if son == 0:
    print("'NOL' qiymat kiritmang!!!")
else: 
  if son>0:
   print("Kiritgan sonningiz MANFIY.")     
  else:
    print("Kiritgan sonningiz MUSBAT.")'''
   
    
'''son=int(input("Son kiriting? "))
if son == 0:
    print("'NOL' qiymat kiritmang!!!")
else: 
  if son>0:
   print("Kiritgan sonningizni kvadrat ildizi>>>.", son**(1/2))     
  else:
    print("Musbat son kiriting!!!.")'''
    

    
'''juft=int(input("Juft son kiriting >> "))
if juft % 2 == 0:
    print("Raxmat")
else :
    print("Juft son kirit birodar")'''


'''yosh = int(input("Yoshingizni kiriting ? "))
if yosh<4 or yosh>60:
    print("Kirish tekin") 
elif yosh<18:
    print("Blet 1000 sum")
else:
    print("Blet 2000 sum")'''



mahsulotlar=["osh", "baliq", "jiz", "shashlik", "manti", "shurbo", "kfs", "lagman","tandiri", "somsa"]    
buyrtma=[]
bor_taomlar=[]
yuq_taomlar=[]
for taom in range(5) :
    buyrtma.append(input(f"{taom+1}- Buyurtmani kiriting! ?"))
for b in buyrtma:
    if b.lower() in mahsulotlar:
        bor_taomlar.append(b)
        #print(b.capitalize(), "Bor")        
    else:
        yuq_taomlar.append(b)


print(f"\nBizning restoranda siz tanlagan taomlardan {bor_taomlar}\n")
print(f"Afsus bizning restoranda siz tanlagan taomlardan {yuq_taomlar} lar yo\'q")    



'''butun_son=int(input("Butun son kiriting >>> "))

for son1 in range(2,11):
    if butun_son % son1 == 0:
        print(f"{butun_son } soni {son1} ga qoldiqsiz bo\'linadi")'''


    
    
    
    
        