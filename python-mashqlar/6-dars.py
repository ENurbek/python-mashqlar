
davlatlar=["uzbekistan", "Qazoqiston", "Qirg'iziston", "Tojikiston", "Turkmaniston"]
print(davlatlar)

print(len(davlatlar))

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)

#print(sort(reverse=True)
print(davlatlar.sort(reverse=True))

#print(davlatlar)
      
sonlar=[]
sonlar=list(range(120, 1200, 2))
print(sonlar)
print(sum(sonlar))
katta=max(sonlar)
kichik=min(sonlar)
ayirma=katta-kichik
print(katta)
print(kichik)
print(ayirma)
print(len(sonlar))
print(sonlar[:5])
print(sonlar[20:25])
print(sonlar[535:])

taomlar=["osh", "shashlik", "manti", "dimlama", "baliq"]
print(taomlar)
nonushta=taomlar[:]
del nonushta[2]
nonushta.remove("osh")
nonushta.append("sut")

print(nonushta)
nonushta=tuple(nonushta)
nonushta[0]="qaymoq"
print(nonushta)