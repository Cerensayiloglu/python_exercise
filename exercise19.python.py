import random
deger=int(input("aklınızdan bi rsayı tutun ve yazın 1 den 100 kadar"))
deneme=0
while deneme<10:

 sayı2=random.randint(1,100)
 if deger==sayı2:
  print(f"teprikler dogru tahmin ettin ")
  break
 
 else:
  print ("yanlıs tahmin tekrar dene")
  deneme+=1


