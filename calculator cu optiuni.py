print("Pt suma selectati 0")
print("Pt diferenta selectati 1")
print("Pt produs selectati 2")
print("Pt raport selectati 3")

n=int(input("Introduceti optiunea dorita: "))
a=float(input("Introduceti primul numar: "))
b=float(input("Introduceti al doilea numar: "))

if(n==0) :
 sum=a+b
 print("Suma este : ",sum)

if(n==1) :
 dif=a-b
 print("Diferenta este : ",dif)   

if(n==2) :
 prod=a*b
 print("Produsul este : ",prod)

if(n==3) :
 raport=a/b
 print("Raportul este : ",raport)   


   

