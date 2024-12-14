from socket import *
import time

# tempo inicial
tempo_inicial = time.time()

alvo = input("informe o IP para ser secanneado: ")

ip_alvo = gethostbyname(alvo)

print("Comecando scan: ",ip_alvo)

for i in range(50,500):
    #IPv4
    # #TCP
    s = socket (AF_INET, SOCK_STREAM)

    #Tento me conectar na porta
    conexao = s.connect_ex((ip_alvo, i))

    if conexao == 0:
        print("Porta: ",i, "aberta")
    s.close()
print("Tempo que levou: ",time.time() - tempo_inicial) 