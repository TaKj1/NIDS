from scapy.layers.inet import TCP, IP
from ..database import add_to_database

def process_ftp_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and packet[TCP].payload:
        ip_address = packet[IP].src
        raw_payload = packet[TCP].load  # Extracting the raw payload
        
        try:
            payload_str = raw_payload.decode("utf-8")  # Decoding the raw payload
        except UnicodeDecodeError:  # In case the payload cannot be decoded
            payload_str = str(raw_payload)
        
        print(f"[DEBUG] FTP Payload: {payload_str}")  # Debug line
        
        if "anonymous" in payload_str:
            print("[DEBUG] Detected 'anonymous' in payload.")
            add_to_database(ip_address, "anonymous")
        elif "530" in payload_str:  # 530 is a common FTP error code for login failure
            print("[DEBUG] Detected '530' in payload.")
            username = "unknown"
            add_to_database(ip_address, username)
