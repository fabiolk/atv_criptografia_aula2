#! /usr/bin/env python

import socket
import sys
import time
import threading
import select
import traceback

from cryptography.fernet import Fernet #biblioteca fonte https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet
key = 'jM0KRW-bDse15vXu8Nf6B0r1fgdeyJSN73eIM3sIJV8=' #variavel estatica
#key = Fernet.generate_key() #usado para gerar a chave acima
print(key)#
class Server(threading.Thread):
    def initialise(self, receive):
        self.receive = receive

    def run(self):
        lis = []
        lis.append(self.receive)
        while 1:
            read, write, err = select.select(lis, [], [])
            for item in read:
                try:
                    s = item.recv(1024)
                    if s != '':
                        chunk = s
                        
                        f = Fernet(key) #instancia f com a chave gerada
                        
                        decrypt_chunk = f.decrypt(chunk)
                        #Decrypts a Fernet token sendo chunk a mensagem recebida no servidor
                        
                        print(decrypt_chunk.decode() + '\n>>')#printa a msg descriptografada
                except:
                    traceback.print_exc(file=sys.stdout)
                    break


class Client(threading.Thread):
    def connect(self, host, port):
        self.sock.connect((host, port))

    def client(self, host, port, msg):
        sent = self.sock.send(msg)
        # print "Sent\n"

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            host = input("Enter the server IP \n>>")
            port = int(input("Enter the server Destination Port\n>>"))
        except EOFError:
            print("Error")
            return 1

        print("Connecting\n")
        s = ''
        self.connect(host, port)
        print("Connected\n")
        user_name = input("Enter the User Name to be Used\n>>")
        receive = self.sock
        time.sleep(1)
        srv = Server()
        srv.initialise(receive)
        srv.daemon = True
        print("Starting service")
        srv.start()
        while 1:
            # print "Waiting for message\n"
            msg = input('>>')
            if msg == 'exit':
                break
            if msg == '':
                continue
            # print "Sending\n"
            msg = user_name + ': ' + msg                    
            
            data = msg.encode()
            
            f = Fernet(key)#instancia f com a chave gerada
            
            encrypt_msg = f.encrypt(data)#Encrypts data passed. The result of this encryption is known as a “Fernet token” and has strong privacy and authenticity guarantees.            
            
            self.client(host, port, encrypt_msg)#envia a mensagem criptografada
        return (1)


if __name__ == '__main__':
    print("Starting client")
    cli = Client()
    cli.start()
