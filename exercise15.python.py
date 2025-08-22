import time
baslangıc=time.time()
while True:
    bitis=time.time()
    sonuc=bitis-baslangıc
    print(f"zaman:{sonuc}")
    secim=input("devam etmek için enter e bas cıkmak istiyorsan q ya bas")
    if secim=="q":
        break
    
    