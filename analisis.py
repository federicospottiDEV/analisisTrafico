from scapy.all import sniff, IP

MAX_PAQUETES = 2000

# Diccionario para traducir el número de protocolo a nombre
PROTOCOLOS = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
    47: "GRE",
    50: "ESP"
}

ipTraficoEntrada = {}
ipTraficoSalida = {}

# Contador de protocolos
conteo_protocolo = {}

def mostrar_paquete(packet):
    if packet.haslayer(IP):
        capa_ip = packet[IP]
        protocolo_num = capa_ip.proto
        protocolo_nombre = PROTOCOLOS.get(protocolo_num, f"Otro ({protocolo_num})")
        ipEntrada= capa_ip.src 

        # Contar protocolo
        if protocolo_nombre in conteo_protocolo:
            conteo_protocolo[protocolo_nombre] += 1
        else:
            conteo_protocolo[protocolo_nombre] = 1


        # Contar ip entrada
        if ipEntrada in ipTraficoEntrada:
            ipTraficoEntrada[ipEntrada] += 1
        else:
            ipTraficoEntrada[ipEntrada] = 1



       # print(f"De: {capa_ip.src} -> A: {capa_ip.dst} | Protocolo: {protocolo_nombre} | Tamaño: {len(packet)} bytes")
    else:
        print("Paquete sin capa IP")


def obtenerCantidad(par):
    return par[1]

# Captura de paquetes
sniff(filter="ip", prn=mostrar_paquete, count=MAX_PAQUETES)

# Mostrar resumen
print("\nResumen de protocolos:")
for protocolo, cantidad in conteo_protocolo.items():
    print(f"{protocolo}: {cantidad} paquetes")


ordenadoEntrada = sorted(ipTraficoEntrada.items(), key = obtenerCantidad, reverse= True) 

print("\n:")
for i in range(5):
    print(f"{ordenadoEntrada[i][0]}: {ordenadoEntrada[i][1]} paquetes")
