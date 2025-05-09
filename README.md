Este challenge es una herramienta simple de análisis de tráfico de red utilizando Python y Scapy. Captura paquetes IP y genera estadísticas:


**funcionamiento**\
La aplicación captura 100 paquetes de red por ejecución (puede configurarse). 
al ejecutarse en un entorno local, la cantidad de paquetes es reducida, por lo que se establece en pocos paquetes para evitar demoras en espera de trafico
Analiza únicamente paquetes con capa IP (IPv4).



**Por cada paquete capturado, se extraen los siguientes datos:**\
1 Dirección IP de origen\
2 irección IP de destino\
3 Protocolo utilizado (TCP, UDP, ICMP, etc.)\
4 Tamaño del paquete en bytes\
5 Tamaño del paquete en bytes


**Al finalizar, muestra un resumen con:**\
Cantidad de paquetes por protocolo.\
Principales IPs de origen y destino por tráfico






**GUIA DE INSTALACION:**

1- clonar el repositorio en tu carpeta:\
git clone https://github.com/federicospottiDEV/analisisTrafico.git\

2- contruir la imagen de docker:\
docker build -t analisistrafico .


**GUIA DE EJECUCCION**

docker run --rm --cap-add=NET_ADMIN --net=host analisistrafico

--cap-add=NET_ADMIN: Habilita permisos de red necesarios para capturar paquetes. la alternativa de esto es instalar npcap en tu equipo en caso de entorno windows\
--net=host: Usa la red del host



 **Requisitos**
Docker instalado

Permisos de administrador (necesarios para acceder a la interfaz de red)


