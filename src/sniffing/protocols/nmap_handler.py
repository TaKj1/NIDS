from scapy.layers.inet import TCP, IP
from ..database import add_to_databaseNMAP

def process_nmap_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        ip_address = packet[IP].src
        
        # Detect SYN scan
        if tcp_layer.flags == 2:  # Only SYN flag is set
            print(f"[!] Detected potential SYN scan from: {ip_address}")
            add_to_databaseNMAP(ip_address,type="Potential SYN scan")
        # Detect NULL scan
        elif tcp_layer.flags == 0:
            print(f"[!] Detected potential NULL scan from: {ip_address}")
            add_to_databaseNMAP(ip_address,type="Potential NULL scan")
        # Detect Xmas Tree scan
        elif tcp_layer.flags == 41:  # FIN, URG, PSH flags set
            print(f"[!] Detected potential Xmas Tree scan from: {ip_address}")
            add_to_databaseNMAP(ip_address,type="Potential Xmas tree scan")

