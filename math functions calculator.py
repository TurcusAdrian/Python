import math
print("....................................")
print("0 este pentru rotunjire")
print("1 este pentru rotunjire in sus")
print("2 este pentru rotunjire in jos")
print("3 este pentru modulul numarului")
print("4 este pentru ridicarea la putere")
print("5 este pentru radicalul numarului")
print("....................................")

n=int(input("introduceti optiunea preferata: "))
a=float(input("introduceti numarul dvs: "))

if(n==0):
    print("rotinjitu la cea mai apropiata valoare intreaga este:", round(a))

if(n==1):
    print("rotunjitul in sus este:", math.ceil(a))

if(n==2):
    print("rotunjitul in jos este:", math.floor(a))

if(n==3):
    print("Numarul in modul este:", abs(a))

if(n==4):
    p=float(input("introduceti puterea la care sa fie ridicat numarul ales initial(a)"))
    print("numarul ridicat la puterea p este:", pow(a,p))

if(n==5):
    print("radicalul numarului este:", math.sqrt(a))


