n=int(input("Introduceti numarul de zile: "))
if (n>=28 ) and (n<=31) :
    if (n==30):
        print('Aprilie, Iunie, Septembrie, Noiembrie')
    if (n==28) or (n==29) :
        print('Februarie')   
    else:
        print('Decembrie, Octombrie, Iunie, August, Martie, Mai, Ianuarie')
else:
        print('Nu exista luna cu asa numar de zile')    