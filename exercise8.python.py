soru1="1 yılda 4 mevsim vardır"
soru2=" köpekler aslannın soyundan gelir"
soru3="kediler uzaylıdır"
sınav={}

sınav[soru1]="doğru"
sınav[soru2]="yanlış"
sınav[soru3]="doğru"
puan=0
while True:

    print("her soru puanı 30 puandır soruları cevaplayın")
    for soru,cevap in sınav.items():
     kullanıcı=input(f" soru:{soru}")
     if sınav[soru]==kullanıcı:
        puan+=30
        print(f"teprikler bi soruyu dogru tahmin ettin puan:{puan}")
     else:
        print(f"malesef soruyu doğru bilemedin puan:{puan}")
    
    devam = input("Tekrar denemek ister misiniz? (e/h): ")
    if devam.lower() == "h":
        break
print(f"puan:{puan}")
   
    
   