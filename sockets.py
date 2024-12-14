import socket

url = input("Digite uma urla: ")

ip = socket.gethostbyname(url)

print(ip)
print(socket.getservbyname("http"))