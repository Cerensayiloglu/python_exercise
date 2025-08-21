#listedeki sayıları tek ve çift olarak ayırma
liste=[1,2,3,4,5,6,7,8,9,12,11,13,14,151,16,17]
cift=[]
tek=[]

for i in liste:
    if i%2==0:
        cift.append(i)
    else:
        tek.append(i)
print(f"tek sayılar:{tek}")
print(f"çift sayılar:{cift}")