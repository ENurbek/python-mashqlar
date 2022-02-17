# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:44:30 2021

@author: 1
"""

'''def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
salom_ber()    '''



'''def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber("Asad")    '''


'''def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
yosh_hisobla('olim', 1997)    '''


'''def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
yosh_hisobla(1995,2020)
yosh_hisobla(1993)    '''




def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(tyil)