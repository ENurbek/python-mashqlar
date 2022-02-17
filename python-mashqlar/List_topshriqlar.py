# -*- coding: utf-8 -*-
"""
Created on Tue May 25 19:32:30 2021

@author: 1
"""

ismlar= ['Asad','Abish','Nurik']
print(f"Salom {ismlar[0]}, bugun dars bormi?")
print(f"{ismlar[1]} bugun qaysi darslar bor?")
print(f"{ismlar[2]} darsing tugadimi?")




sonlar= [2, 4, 6.4, -5, 6]
print(sonlar)
print(sonlar[2]+sonlar[0])
print(sonlar[3]-sonlar[4])
print(sonlar[2-1]+sonlar[3])
sonlar[2]=5
sonlar[1]=5
print(sonlar)



t_shaxslar=['Temur','Bobur','Alisher']
z_shaxslar=['Ilen','Bezzos','Bell']
t_shaxs= t_shaxslar.pop(1)
z_shaxs= z_shaxslar.pop(0)
print("Men","",f"{t_shaxs}ni kitobini o\'qidim")
print(f'Men {z_shaxs}ni ishlariga qiziqaman.')


friends= []
friends.append("Asad")
friends.append("Abish")           
friends.append("Nurik")
friends.append("Maxa")
friends.append("Fera")
print("Darsga keladiganlar ro\'yxati, ", friends)
friends.remove("Fera")
friends.remove("Maxa")
print("Darsga kelganlar ", friends)
friends.append("Shaxlo")
friends.insert(0, "Milamush")
friends.insert(2, "Maxmud")
print("Sinfdagilarni xammasi ", friends)

#friends=['dadsd','sddsds','sdsdada','sfregf','sgtggrhr','rteteytge']
mehmonlar= []
mehmonlar=[friends.pop(0)]
mehmonlar.append(friends.pop(4))
mehmonlar.append("Fera")
print("Keladigan mehmonlar", mehmonlar)










