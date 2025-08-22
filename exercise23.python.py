#Sayıları farklı tabanlara çevirme (ikilik, sekizlik)

def cevir(sayı,taban):
    sonuc=""
    kalan=sayı%taban
    sonuc=str(kalan)+sonuc
    sayı//=taban
    return sonuc
sayi=int(input("bir sayı girin"))
print(f"İkilik : {cevir(sayi, 2)}")
print(f"Sekizlik (octal): {cevir(sayi, 8)}")

