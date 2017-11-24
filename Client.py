import socket
from thread import *
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8889))
u = raw_input('Username: ')

print 'Para enviar: Destinatario>Mensaje'



def se(s):
    if raw_input("Para ver comandos ingresar: commands\n") == "commands":
        print "show_users_online                Para mostar usuarios concectados"
        print "chat                             Para abrir conversacion con un usuario"
        print "chat2                            Para crear grupo con uno o mas usuarios"
        print "send_file                        Para enviar un archivo a uno o mas usuarios"
        print "\n"

        inp = raw_input()
        if inp == "show_users_online":
            s.send("show_users_online")

        if inp == "chat":
            name = raw_input("Ingrese nombre: ")
            sender = name + '>'
            while 1:

                print "\n"+sender
                s.send(sender + sender + raw_input())
                #print s.recv(1024)
               # if raw_input() == "quit":
                #    start_new_thread(se, (s,))
                 #   start_new_thread(re, (s,))
                 #   break

        if inp == "chat2":
            while 1:
                s.send(u + '>' + raw_input())
                print s.recv(1024)
                #if raw_input() == "quit":
                 #   start_new_thread(se, (s,))
                  #  start_new_thread(re, (s,))
                  #  break
        if inp == "send_file":
            f = raw_input("Ingrese ruta del archivo: ")
            with open(f, 'wb') as file_to_write:
                while True:
                    data = s.recv(1024)
                    if not data: break
                    file_to_write.write(data)
                    file_to_write.close()
                    break
            #bytes = open(f).read()
            #s.send(bytes)

def re(s):
    while 1:
        s.send(u + '>show>')
        r = s.recv(1024)
        if r != 'No messagesOk' and r != 'No messages' and r != 'No messagesNo messages' and r != "OkNo messages":
            print r
        sleep(0.05)

start_new_thread(se ,(s,))
start_new_thread(re ,(s,))
while 1:
    pass
