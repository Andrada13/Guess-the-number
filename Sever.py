import socket
import random


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #creare socket,AF_INET este pentru internet, SOCK_STREAM este pentru protocolul de transport TCP
s.bind(("127.0.0.1",1200)) #leaga socketul la adresa si port
s.listen(2) #numarul de conexiuni acceptate, asteapta sa se conecteze clientii 

(c,a) = s.accept() #conexiunea este acceptata, este stabilita cu clientul
print ("Conexiunea a inceput ", a)

Hello=c.recv(10000).decode() #acceptam informatiile,primeste mesajele 

print(Hello)

ghiceste="GHICESTE !" #trimite mesajul catre client
c.send((ghiceste+"\r\n").encode()) #trimite mesajul

game=c.recv(10000).decode() #primeste mesajul
print (game)

ready="Jocul a inceput !"
c.send((ready+"\r\n").encode()) #trimite mesajul

tries=0 #initializam numarul de incercari cu 0
cifru = random.randint(1, 100) #genereaza un numar random intre 1 si 100
print("Numarul generat de server este : ",cifru) #afisam numarul generat random de catre server

running = 1 #setam running ca fiind adevarat 

while running:
    numar=c.recv(10000).decode()
    numar=int(numar)
    print(numar)
    tries+=1 #incrementam numarul de incercari

    if numar < cifru:

        message1="PREA MIC ! INCEARCA DIN NOU !"
        c.send((message1+"\r\n").encode())

    if numar > cifru:

        message2="PREA MARE ! INCEARCA DIN NOU !"
        c.send((message2+"\r\n").encode())

    if (numar==cifru):

        correct="AI GHICIT !"
        c.send((correct+"\r\n").encode())
        print("AI GHICIT DIN", tries ,"INCERCARI !")

        running=0 #dupa ce numarul a fost ghicit running devine adevarat

c.close() #conexiunea se inchide 