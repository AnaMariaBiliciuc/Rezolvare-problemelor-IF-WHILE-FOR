from fractions import Fraction 
n=int(input("Introduceti numaratorul  primei fractii: "))
m=int(input("Introduceti numitorul primei fractii: "))
l=int(input("Introduceti numaratorulfractiei a2: "))
p=int(input("Introduceti numitorul  fractiei a2: "))
print(Fraction(n ,m) + Fraction(l, p))
print(Fraction(n,m) * Fraction(l,p))
