from socket import *

endereco = "127.0.0.1"
porta = 42310

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((endereco, porta))
obj_socket.listen(2)
print("Aguardandon Cliente...")

while True:
    conexao, cliente = object.accept()
    print("Conectado com ", cliente)

    while True:
        mensagem = str(conexao.recv(1024))
        print("recebi", str(Mensagem)[2-1])

        msg = bytes(input("Mensagem: "), "utf-8")
        conexao.send(msg)
        break
              
    conexao.close()