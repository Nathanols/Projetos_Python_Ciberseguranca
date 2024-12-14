from socket import *
import logging
from datetime import datetime

logging.basicConfig(filename = "honeypot.log", level = logging.INFO, format = '%(asctime)s - %(message)s')

def iniciar_honeypot(endereco,porta):
    meu_socket = socket(AF_INET,SOCK_STREAM)

    meu_socket.bind((endereco,porta))

    meu_socket.listen(5)

    print("Honeypot rodando no endereco e porta: ", endereco, porta)

    while True:
        socket_cliente, endereco_cliente = meu_socket.accept()

        logging.info("Conexão vinda de: ",endereco_cliente)
        socket_cliente.close()

        logging.info(f"Conexão de {endereco_cliente}")

iniciar_honeypot("127.0.0.1",8080)