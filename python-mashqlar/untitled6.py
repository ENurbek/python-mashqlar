# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:37:17 2021

@author: 1
"""
# =============================================================================
# while True:
# import random
# 
# a=random.randint(1,10)
# print(a)
# uylangan_son=int(input("1 dan 10 gacha son o'yladim. Topa olasizmi?>>"))
# hisob_odam=0
# 
# while True:
#     hisob_odam+=1
#     if a==uylangan_son:
#         print(f"\nTOPDINGIZ! {a} sonini o'ylagan edim. {hisob_odam} ta taxmin bilan topdingiz tabriklayman!! " )
#         break
#     elif a>uylangan_son:
#         uylangan_son=int(input("Xato, men o'ylagan son bundan kattaroq. yana harakat qiling:>>"))
#     else:
#         uylangan_son=int(input("Xato, men o'ylagan son bundan kichkroq. yana harakat qiling:>>")    )
#         
# davom_ettirish=input("\n1 dan 10 gacha son o'ylang men topishga xarakat qilaman.\n"
#       "\tO'ylagan bo'lsangiz UZUN TUGMANI BOSING va ENTER ni bosing.")
# if davom_ettirish==" ":
#     
#     q=1
#     w=10
#     hisob_k=0
#     while True:
#         hisob_k+=1
#         k=random.randint(q,w)
#         print(f"\nSiz {k} sononi o'yladingiz:")
#         l=input("\nTo'g'ri ('t'), men o'ylagan son bundan kattaroq ('+'), yoki kichikroq('-') ")
#         
#         if l=="t":
#             #print(f"TOPDINGIZ! {a} sonini o'ylagan edim. {s} ta taxmin bilan topdingiz tabriklayman!! " )
#             print(f"\nMen {hisob_k} urunishda topdim")
#             break
#         elif l=="-":
#             w=k
#         else:
#             l=="+"
#             q=k
#     if hisob_odam==hisob_k:
#         print(f"({hisob_odam}:{hisob_k}) Durang!!!")
#     elif hisob_odam>hisob_k:
#         print(f"({hisob_odam}:{hisob_k}) Men yutdim 'URRA'")
#     else:
#         print(f'({hisob_odam}:{hisob_k}) Siz yutdingiz "TABRIKLAYMAN!!!')    
# 
# d=input("Yana o'ynaymizmi?")    
# 
# =============================================================================


while True:
    import random

    a=random.randint(1,10)
   # print(a)
    uylangan_son=int(input("1 dan 10 gacha son o'yladim. Topa olasizmi?>>"))
    hisob_odam=0
    while True:
        hisob_odam+=1
        if a==uylangan_son:
            print(f"\nTOPDINGIZ! {a} sonini o'ylagan edim. {hisob_odam} ta taxmin bilan topdingiz tabriklayman!! " )
            break
        elif a>uylangan_son:
            uylangan_son=int(input("Xato, men o'ylagan son bundan kattaroq. yana harakat qiling:>>"))
        else:
            uylangan_son=int(input("Xato, men o'ylagan son bundan kichkroq. yana harakat qiling:>>")    )
    
    davom_ettirish=input("\n1 dan 10 gacha son o'ylang men topishga xarakat qilaman.\n"
      "\tO'ylagan bo'lsangiz UZUN TUGMANI BOSING va ENTER ni bosing.")
    if davom_ettirish==" ":
         q=1
         w=10
         hisob_k=0
    while True:
             hisob_k+=1
             k=random.randint(q,w)
             print(f"\nSiz {k} sononi o'yladingiz:")
             l=input("\nTo'g'ri ('t'), men o'ylagan son bundan kattaroq ('+'), yoki kichikroq('-') ")
        
             if l=="t":
            #print(f"TOPDINGIZ! {a} sonini o'ylagan edim. {s} ta taxmin bilan topdingiz tabriklayman!! " )
                print(f"\nMen {hisob_k} urunishda topdim")
                break
             elif l=="-":
                  w=k
             else:
                  l=="+"
                  q=k
    if hisob_odam==hisob_k:
        print(f"({hisob_odam}:{hisob_k}) Durang!!!")
    elif hisob_odam>hisob_k:
        print(f"({hisob_odam}:{hisob_k}) Men yutdim 'URRA'")
    else:
        print(f'({hisob_odam}:{hisob_k}) Siz yutdingiz "TABRIKLAYMAN!!!')    

#d=input("Yana o'ynaymizmi?")    
    
   
    
   
    surov=input("Yana o'ynaysizmi? (Yes/No)")
    if surov=="Yes":
        print("               BARDAM BO'LING.")
    else:
        print("HAYIR.")
        break
    
    

    