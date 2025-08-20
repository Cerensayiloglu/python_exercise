import random
#bu projede  rastgele bir şekilde sifre olusturuluyo ve sonra bu oluşturulan şifre kırılmaya calisiyor
liste=["a","b","c","d","e","1","2","3","4","5","6","*",".",",","/"]#şifre oluştururken kullanabilecek belirli değerler
password=""
for i in range(1,5):#sifre kaç haneli olucak
    value=random.choice(liste)#rastgele listeden belirlenen değerlerden rastgele bi tane secicek ve bunu value degerine esitlicek
    password=password+value
deneme=0
while True:# şifre kırılana kadar döngü devam edicek
 password2=""
 for i in range(1,5):
    value2=random.choice(liste)
    password2=password2+value2
    deneme+=1
    if password==password2:#
        print(f"şifreniz kırıldı şifre:{password} {deneme} denemede bulundu")
        break#şifre bulunduğunda döngüden çıkıyor
    elif deneme%100==0:#her yüz denemede bir kac kerew şifreyi kırmayı denediğini gösterecek
        print(f"işlem devam ediyor {deneme} deneme sayısı kadar denendi ama hala kırılmadı")