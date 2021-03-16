import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #creare socket,AF_INET este pentru internet, SOCK_STREAM este pentru protocolul de transport TCP
s.connect(('127.0.0.1',1200)) #se conecteaza la server



input("Tasteaza start pentru a incepe jocul : ") #clientul trimite mesajul START catre server
start="START"
s.send((start +"\r\n").encode()) #transmite mesajul catre server

greetings=s.recv(10000).decode()
print(greetings)

titlu="Ghiceste cifrul ! "
s.send((titlu +"\r\n").encode())

titlu=s.recv(10000).decode()
print (titlu)


running=1

while running:

    c = input("Introduceti un numar: ") #jucatorul trimite serverului un numar introdus de la tastatura
    s.send(c.encode())
    

    response = s.recv(10000).decode()
    print(response)
    if response.startswith("AI GHICIT !"):
              running = 0



s.close() #inchide socketul