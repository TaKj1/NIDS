from scapy.all import sniff

def packet_callback(packet):
    # Print out the raw packet data for now
    print(packet)

def main():
    # Capture packets in promiscuous mode
    # If you run into any permission issues, you may need to run the script with administrative rights
    sniff(prn=packet_callback, store=0, iface="enp8s0", filter="", count=0)

if __name__ == "__main__":
    main()
