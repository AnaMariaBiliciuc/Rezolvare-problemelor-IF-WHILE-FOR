from math import log
m=int(input("Introduceti nr m: "))
n=int(input("Introduceti nr n: "))
n> m
i= log(n,m)
l= int(i)
if i-l==0 :
    print("Numarul n este puterea lui m")
else:
    print("Numarul n nu este puterea lui m")