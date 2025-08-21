not_defteri={}
while True:
   print("eklemelk istiyorsan-->1")
   print("notları göster -->2")
   print("listelemek istiyorsanız-->3")
   isaret=int(input("seciminizi yapın"))
   if isaret ==1:
      isim=input("ismi girin")
      note=input("notunuzu girin")
      not_defteri[isim]=note
      
      
   elif  isaret==2:
      if not not_defteri:
         print("henüz öğrenci eklenmedi")
      else:
         for isim,notu in not_defteri.items():
            print(f"isim:{isim} notu:{notu}")
   elif isaret==3:
      print("sistemden çıkılıyor")
      break

      


  
