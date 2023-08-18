from scapy.all import *
from .protocols import ftp_handler
from scapy.layers.inet import TCP, IP
from .database import setup_database

if 1 == 1:
 setup_database()


def get_interface_list():
    interfaces = []
    with open('/proc/net/dev', 'r') as file:
        lines = file.readlines()[2:]  # Skip the first two lines
        for line in lines:
            interface = line.split(':')[0].strip()
            interfaces.append(interface)
    return interfaces

def packet_callback(packet):
    # For FTP packets (on port 21), we'll process them using ftp_handler
    if packet.haslayer(TCP) and (packet[TCP].dport == 21 or packet[TCP].sport == 21):

        
        ftp_handler.process_ftp_packet(packet)
    else:
        # Print out the raw packet data for the other protocols
        print(packet)

def select_interface():
    interfaces = get_interface_list()
    
    print("Available network interfaces:")
    for index, interface in enumerate(interfaces, start=1):
        print(f"{index}. {interface}")

    while True:
        choice = input("Select an interface by number (e.g., 1): ")
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(interfaces):
                return interfaces[choice - 1]
            else:
                print("Invalid selection. Please select a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    selected_interface = select_interface()
    # Capture packets in promiscuous mode
    fitler_string = "tcp port 21 "
    sniff(prn=packet_callback, store=0, iface=selected_interface, filter=fitler_string, count=0)


if __name__ == "__main__":
    main()
