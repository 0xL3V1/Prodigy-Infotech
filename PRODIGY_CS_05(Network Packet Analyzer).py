from scapy.all import *
import netifaces


# Function to analyze packets
def analyze_packets(packet):

    if IP in packet:
        source_ip_address = packet[IP].src
        destination_ip_address = packet[IP].dst
        
        if TCP in packet:
            # TCP packet
            destination_port = packet[TCP].dport
            payload_size = len(packet[TCP].payload)
            print(f"TCP  -> from IP = {source_ip_address}:{packet[TCP].sport} To IP = {destination_ip_address}:{destination_port}   size: {payload_size} bytes AND the Packet is \n{packet[TCP].payload}\n")
        
        elif UDP in packet:
            # UDP packet
            destination_port = packet[UDP].dport
            payload_size = len(packet[UDP].payload)
            print(f"UDP  -> from IP = {source_ip_address}:{packet[UDP].sport} To IP = {destination_ip_address}:{destination_port}   size: {payload_size} bytes AND the Packet is \n{packet[UDP].payload}\n")
        
        else:
            # IP packet without TCP or UDP
            print(f"IP -> from IP = {source_ip_address} To IP = {destination_ip_address}")

# Get the list of network interfaces
network_interfaces = netifaces.interfaces()

# Print the list of available interfaces
for interface in network_interfaces:
    if interface != 'lo': 
        print(interface)

# User input for the interface to analyze
interface_name = input("what is the Interface You want to analyze ENTER THE EXACT NAME:\n")

# Check if the entered interface exists
if interface_name in network_interfaces:
    print(" packet sniffer ")
    # Sniff packets on the specified interface and call the 'analyze_packets' function
    sniff(iface=interface_name, prn=analyze_packets)
else:
    print("the Interface is not found")
