print("ULTIMATE BEGGINER'S GUESSING GAME")
print(" ")
print(" ")
print(" ")
print("Tastati 1 pentru a incepe")
print("Tastati 2 pentru a iesi")
print("Tastati 3 pentru regulile jocului")
n=int(input("optiunea selectata:"))
scor=0

if(n==1):
    print("Incepere joc...")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    print("1.Care este cel mai inalt varf din Romania?")
    print("a.Vf Negoiu  b.Vf Moldoveanu  c.Vf Omu  d.Vf Lespezi")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="b"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1

    elif((m=="a")|(m=="c")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: b")
        print(" ")
        scor=0

    print("2.Care este resedinta judetului Timis?")
    print("a.Timisoara  b.Lugoj  c.Sanicolau  d.Beba Veche")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="a"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1

    elif((m=="b")|(m=="c")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: a")
        print(" ")

    print("3.Unde a domnit Stefan cel Mare?")
    print("a.Ucraina  b.Transilvania  c.Moldova  d.Tara Romaneasca")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="c"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1

    elif((m=="a")|(m=="b")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: c")
        print(" ")    

    print("4.Capitala statului Italia este?")
    print("a.Paramaribo  b.Budapesta  c.Paris  d.Roma")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="d"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1

    elif((m=="a")|(m=="b")|(m=="c")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: d")
        print(" ")

    print("5.Care este autorul cartii 'Tom Saywer'?")
    print("a.Jules Verne  b.Howard Phillips Lovecraft  c.Mark Twain  d.Agatha Christie")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="c"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
    
    elif((m=="a")|(m=="b")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: c")
        print(" ")

    print("6.Care este cel mai mare patrat perfect mai mic ca 10?")
    print("a.9  b.2  c.5  d.7")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="a"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
    
    elif((m=="b")|(m=="c")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: a")
        print(" ")

    print("7.In ce se masoara greutatea?")
    print("a.kilogram  b.metru  c.newton  d.candela")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="c"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
    
    elif((m=="a")|(m=="b")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: c")
        print(" ")

    print("8.Cine este presedintele Romaniei?")
    print("a.Traian Basescu  b.Klaus Iohannis  c.Liviu Dragnea  d.Dan Barna")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="b"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
    
    elif((m=="a")|(m=="c")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: b")
        print(" ")

    print("9.Care este cel mai lung os din corpul uman?")
    print("a.femurul  b.humerus  c.stern  d.tibia")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="a"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
    
    elif((m=="b")|(m=="c")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: a")
        print(" ")

    print("10.Cine canta piesa 'Locked Up'?")
    print("a.Sean Paul  b.Micheal Jackson  c.Akon & Styles P  d.Eminem & Dr Dre")
    print(" ")
    m=input("varianta aleasa:")

    if(m=="c"):
        print(" ")
        print("Raspuns corect!")
        print(" ")
        scor=scor+1
        print("Scorul final este:",str(scor)+" "+"din"+" "+str(10))
    
    elif((m=="a")|(m=="b")|(m=="d")):
        print(" ")
        print("Raspuns gresit! Raspuns corect: c")
        print(" ")
        print("Scorul final este:",str(scor)+" "+"din"+" "+str(10))

    if(scor>=7):
        print("Doriti sa continuati la nivelul mediu?")
    elif(scor<=7):
        print("Joc terminat.Incearca din nou!")

elif(n==2):
    print("joc terminat") 

else:
    print(" ")
    print("Fiecare raspuns corect reprezinta 1 punct")
    print("La un raspuns gresit nu se scad puncte dar nici nu se pun")
    print("Este interzisa cautarea raspunsurilor pe internet sau in alta parte")
    print("Daca scorul obtinut dupa primele 10 intrebari este mai mare de 7 se trece la nivelul urmator")    
    print("Spor la joc si distractie multa!")
    print(" ")