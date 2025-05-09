from scapy.all import sniff, IP

MAX_PAQUETES = 100


PROTOCOLOS = {
 1: "ICMP",
 6: "TCP",
 17: "UDP",
 47: "GRE",
 50: "ESP"
}

ipTraficoEntrada = {}
ipTraficoDestino = {}
conteo_protocolo = {}



def mostrar_paquete(packet):
    if packet.haslayer(IP):
        capa_ip = packet[IP]

        protocolo_num = capa_ip.proto
        protocolo_nombre = PROTOCOLOS.get(protocolo_num, f"Otro ({protocolo_num})")

        ipEntrada= capa_ip.src 
        ipDestino= capa_ip.dst

        sumarContador(protocolo_nombre, conteo_protocolo)
        sumarContador(ipEntrada, ipTraficoEntrada)
        sumarContador(ipDestino, ipTraficoDestino)

       # en caso de querer ver los paquetes descomentar print(f"De: {capa_ip.src} -> A: {capa_ip.dst} | Protocolo: {protocolo_nombre} | Tamaño: {len(packet)} bytes")
    else:
        print("Paquete sin capa IP")

def sumarContador(a, b):
    if a in b:
        b[a] += 1
    else:
        b[a] = 1
    

sniff(filter="ip", prn=mostrar_paquete, count=MAX_PAQUETES)


print("\nResumen de protocolos:")
for protocolo, cantidad in conteo_protocolo.items():
    print(f"{protocolo}: {cantidad} paquetes")

def obtenerCantidad(par):
    return par[1]

ordenadoEntrada = sorted(ipTraficoEntrada.items(), key = obtenerCantidad, reverse= True) 
ordenadoDestino= sorted(ipTraficoDestino.items(), key = obtenerCantidad, reverse= True) 


# aca printeo las 5 principales ip entrada/destino
print("\n5 direcciones IP de origen con mayor tráfico")
for i in range(min(5, len(ordenadoEntrada))):
    print(f"{ordenadoEntrada[i][0]}: {ordenadoEntrada[i][1]} paquetes")
print("\n5 direcciones IP de destino con mayor tráfico")
for i in range(min(5, len(ordenadoDestino))):
    print(f"{ordenadoDestino[i][0]}: {ordenadoDestino[i][1]} paquetes")

