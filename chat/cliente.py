from socket import *

#           localhost
endereco = "127.0.0.1"
porta = 42310

while True:
    #IPv4  o IPv6
    #AF_INET - IPv4

    #TCP ou UDP
    #TCP - Mais segura e mais lento
    #UDP - Menos seguro e mais rapido
    #SOCKSTREAM - TCP
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((endereco,porta))

    msg = bytes(input("Mensagem: "),'utf-8')
    obj_socket.send(msg)

    resposta = obj_socket.recv(124)
    print("Resposta", str(resposta)[2:-1])
    if str(msg)[2:1] == "fim":
        break
obj_socket.close()
