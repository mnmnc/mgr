#!/usr/bin/env python3

import protocols.protocol as protocol

class ARP(protocol.Protocol):
	"""Class for managing wireshark filters for ARP protocol (Address Resolution Protocol).

	Dependencies:
		Protocol class needs to be imported.

	Properties:
		name - name of protocol
		fields_selected - list of dictionaries
		fields_available - list of dictionaries

	Functions available:
		get_description( name ) 		-> String
		get_names_available() 			-> List	
		get_names_selected() 			-> List
		print( switch )
		print_description( name )
		remove_filed( name ) 			-> Dictionary | None
		select_field( name )
	"""

	def __init__(self):
		self.name = "ARP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "arp.src.hw_mac", 
			"description" : "MAC address of source."
		},
		{
			"name" : "arp.src.proto_ipv4",
			"description" : "IP address of source."
		},
		{
			"name" : "arp.dst.hw_mac",
			"description" : "MAC address of destination."
		},
		{
			"name" : "arp.dst.proto_ipv4",
			"description" : "IP address of destination."
		},
		{
			"name" : "arp.opcode",
			"description" : "1 -> Request. 2 -> Reply. 3 -> Reverse request. 4 -> Reverse reply."
		}
	]

	
