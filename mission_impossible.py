from scapy.all import *
from scapy.layers.inet import *
from socket import *


# Setup packet parameters
target = "CHANGE THIS TO A THING"
agent_name = "Ethan Hunt "
ports = [3, 33, 333, 3333, 33333]

def packet_craft(agent_name, code_attempt, source_port):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    payload = agent_name + code_attempt
    pkt = IP() / UDP(dport=2600) / agent_name
    return pkt


print "Beginning cracking...\n"

# First we craft a large number of packets using a random ephemeral port

for p in ports:
    for i in range(10000):
        pkt = packet_craft(agent_name, i)
        send(pkt)
        print "Sent packet {:d} on port {:d}\n".format(i, p)

print "Done cracking!\n"


