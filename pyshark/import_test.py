#!/usr/bin/env python3

import protocols.protocol as protocol
from protocols import frame, ethernet, arp, ip, tcp, udp, http, dns

# frame, eth, arp, ip, tcp, udp, http, dns

frame = frame.Frame()
ethernet = ethernet.Ethernet()
arp = arp.ARP()
ip = ip.IP()
tcp = tcp.TCP()
udp = udp.UDP()
http = http.HTTP()
dns = dns.DNS()

frame.select_all()

print(frame.get_names_selected())



