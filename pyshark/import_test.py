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
ethernet.select_all()
arp.select_all()
ip.select_all()
tcp.select_all()
udp.select_all()
http.select_all()
dns.select_all()

protocols_list = [ frame, ethernet, arp, ip, tcp, udp, http, dns]

def create_name_list( protocols_list ):
	result_list = []
	for protocol in protocols_list:
		temp_list = protocol.get_names_selected()
		for item in temp_list:
			result_list.append(item)
	return result_list;

def param_string_from_list( p_list, param_prefix ):
	result_string = ""
	for item in p_list:
		result_string = result_string + " " + param_prefix + " " + item + " "
	return result_string

p_list = create_name_list(protocols_list)

print(param_string_from_list(p_list, "-e"))

