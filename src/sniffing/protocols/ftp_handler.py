import re
from scapy.layers.inet import TCP, IP
from ..database import add_to_databaseFTP


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
            add_to_databaseFTP(ip_address, "anonymous")
        elif "530" in payload_str:  # 530 is a common FTP error code for login failure
            print("[DEBUG] Detected '530' in payload.")
            attempt_match = re.search(r"Login incorrect for user (\w+): (\w+)", payload_str)
            if attempt_match:
                username = attempt_match.group(1)  # Capture the matched username
                password = attempt_match.group(2)  # Capture the matched password
                print(f"[DEBUG] Incorrect login attempt with username: {username} and password: {password}")
            else:
                username = "unknown"  # Fallback to 'unknown' if regex match fails
            add_to_databaseFTP(ip_address, username)
