import socket
from thread import *
import string
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8889))
s.listen(10)
c = {}
users = " "

def clientthread(conn):
    while 1:
        data = conn.recv(1024)
        data1 = conn.recv(1025)
        e = data.split('>')
        if len(users) <= 3:
            users.append(e[0])
            data1 = users
        conn.send(data1)  #Data1 tiene que ser string o buffer , no lista
        if len(e) == 3:
            if e[1] == 'show':
                try:
                    m = ''
                    for i in range(0, len(c[e[0]])):
                        m = m + c[e[0]][i]
                        if i != (len(c[e[0]])-1):
                            m = m + '\n'
                        if m == '':
                            data = 'No messages'
                        else:
                            data = m
                    del c[e[0]]
                except:
                    data = 'No messages'
            else:
                try:
                    c[e[1]]
                except:
                    c[e[1]] = []
                c[e[1]].append(e[0]+'>'+e[2])
                #C : Diccionario , Destinatario : Mensaje
                data = 'Ok'
        else:
            data = 'Error'
        conn.send(data)
    conn.close()
while 1:
    conn, addr = s.accept()
    start_new_thread(clientthread ,(conn,))
s.close()