# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 10:53:44 2021

@author: 1
"""

'''def ikkisy(a, b):
    """Ikki soni yigindisi"""
    a=int(input("1- sonni kiriting? "))
    b=int(input("2- sonni kiriting? "))
    print(f"{a}+{b}={a+b}")
ikkisy("a", "b")    '''



'''def ism_yil(ism, yosh):
    """
    
Tugulgan yilingizni aniqlaydigan funksiya
    Parameters
    ----------
    ism : TYPE Maton bulishi kerak
        DESCRIPTION.
    yosh : TYPE Butun son bulishi kerak
        DESCRIPTION.

    Returns
    -------
    None.

    """
    ism=input("Ismingiz nima? ").title()
    yosh=int(input(f"{ism} yoshingizni kiriting? "))
    print(f"{ism} siz {2021-yosh} da tug\'ulgansiz.")
ism_yil("ism", "yosh")   '''






'''def toq_juft(a):
    """toq yoki juftlogini aniqlash funksiyasi"""
    a=int(input("Son kiriting? "))
    if a%2 == 0:
        print(f"{a} juft son.")
    else:
        print(f"{a} toq son.")
toq_juft("a")   '''


'''def kattsini_top(a, b):
    a=input(a)
    b=input(b)
    if a==b:
        print("ikala son teng")
#elif
    elif a>b:
        print(a ,"katta")
    else:
        print(b," katta")
kattsini_top("a", "b")        '''



def bulish(k):
    """1 dan 10 gach qoldiqsiz bulish alomati"""
    k=int(input("Son kiriting? "))
    for i in range(1,11):
        if k%i==0:
            print(k, i," ga qoldiqsiz bulinadi.")
bulish("k")            
    
       
