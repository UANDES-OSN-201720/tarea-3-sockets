import socket
from thread import *
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8889))
u = raw_input('Username: ')

print 'To send: recipient>message'
def se(s):
    if raw_input("Para ver comandos ingresar: commands\n") == "commands":
        print "show_users_online                Para mostar usuarios concectados"
        print "talk_to_'Name'                   Para abrir conversacion con un usuario"
        print "create_group with name1,name2    Para crear grupo con uno o mas usuarios"
        print "send_file_to_name1,name2         Para enviar un archivo a uno o mas usuarios"
        print "\n"

        inp = raw_input()
        if inp == "show_users_online":
            s.send("show_users_online")
        if inp == "talk_to":
            while 1:

                s.send(u + '>' + raw_input())
                print s.recv(1024)
def re(s):
    while 1:
        s.send(u + '>show>')
        r = s.recv(1024)
        if r != 'No messages':
            print r
        sleep(0.05)

start_new_thread(se ,(s,))
start_new_thread(re ,(s,))
while 1:
    pass