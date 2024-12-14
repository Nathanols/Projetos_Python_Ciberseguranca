import scapy.all as scapy

from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface,store=False,prn=processar_pacote)

def processar_pacote(pacote):
    if pacote.haslayer(http.HTTPRequest):
        print(pacote)

sniffing('Ethernet')