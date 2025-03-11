from scapy.all import sniff, IP, TCP, UDP, Ether
import json

packets_info = []

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

      
        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Otro"

       
        packet_info = {
            "ip_origen": ip_src,
            "ip_destino": ip_dst,
            "protocolo": protocol_name,
            "puerto_origen": None,
            "puerto_destino": None,
            "mac_origen": None,
            "mac_destino": None
        }

       
        if TCP in packet:
            packet_info["puerto_origen"] = packet[TCP].sport
            packet_info["puerto_destino"] = packet[TCP].dport
        elif UDP in packet:
            packet_info["puerto_origen"] = packet[UDP].sport
            packet_info["puerto_destino"] = packet[UDP].dport

        
        if Ether in packet:
            packet_info["mac_origen"] = packet[Ether].src
            packet_info["mac_destino"] = packet[Ether].dst

        
        packets_info.append(packet_info)

        
        print(f"Paquete capturado: {ip_src} -> {ip_dst} | Protocolo: {protocol_name}")

        
        if len(packets_info) >= 20:
            raise KeyboardInterrupt  

def start_sniffing():
    print("Iniciando el sniffer... Capturando 20 paquetes.")
    try:
        
        sniff(prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("Captura completada.")

    
    with open("packets.json", "w") as file:
        json.dump(packets_info, file, indent=4)
    print("Información guardada en packets.json")

if __name__ == "__main__":
    start_sniffing()