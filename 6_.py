n= eval(input("Introduceti nr n: "))
s1=0
s2=0
a=0
for i in range (1, (n+1)) :
    s1+= i**3
    a+= i
    s2+= a**2
if s1>s2 :
    print(" Suma unu este mai mare")
if s1==s2 :
    print(" Sumele sunt egale")
else :
    print(" Suma 2 este mai mare ") 


n= eval(input("Introduceti un nr n: "))
s1=0
s2=0
a1=0
a2=0
for i in range (1,(n+1)) :
    a1+=i**2
    s1+=3*(a1)
    a2+=i
    s2+= i**3+ i**2+ a2
if s1>s2 :
    print(" Suma unu este mai mare")
if s1==s2 :
    print(" Sumele sunt egale")
else :
    print(" Suma 2 este mai mare")