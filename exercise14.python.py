sayilar = [5, 2, 9, 1]

for i in range(len(sayilar) - 1):
    print(f"\n{i+1}. TUR")
    for j in range(len(sayilar) - 1 - i):
        if sayilar[j] > sayilar[j+1]:
            sayilar[j], sayilar[j+1] = sayilar[j+1], sayilar[j]
        print(sayilar)  # her adımı yazdır

print("\nSonuç:", sayilar)