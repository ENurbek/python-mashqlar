# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:57:25 2021

@author: 1
"""
s=0
ismlar= ["ali", "vali", "asad", "abish", "nurik"]
for a in list(range(len(ismlar))):
    print(f"{ismlar[a]} salom")
    s=s+1
print("kod", s, "marta takrorlandi")    


sonlar= []
for b in range(11, 100,2):
    sonlar.append(b**3)
print(sonlar)     


kinolar=[]
for d in range(5):
    kinolar.append(input(f"{d+1}-sevgan kinong?"))
print(kinolar)    
    
         