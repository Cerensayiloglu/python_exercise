cumle=input("cümle girin")
liste=cumle.split("")
en_uzun=liste[0]
for kelimeler in liste:
  if len(kelimeler)>len(liste[en_uzun]):
   en_uzun=liste[i]
print(f"en uzun kelime:{en_uzun} kelimenin uzunluğu ise:{len(en_uzun)}") 