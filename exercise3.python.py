#this project create pasword
import random
number=int(input("How many digits will your password have?"))
liste=["a","b","c","d","e","1","2","3","4","5","6","*",".",",","/"]
password=""
for i in range(1,number+1):
    value=random.choice(liste)
    password=password+value
print(f"paasword is:{password}")

    
