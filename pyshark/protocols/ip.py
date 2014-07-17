#!/usr/bin/env python3
import protocols.protocol as protocol

class IP(protocol.Protocol):
	"""Class for managing wireshark filters for IP protocol (Internet Protocol).

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
		self.name = "IP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "ip.src", 
			"description" : "IP address of source."
		},
		{
			"name" : "ip.dst",
			"description" : "IP address of destination."
		},
		{
			"name" : "ip.ttl",
			"description" : "TTL - time to live of packet. Decreased by every Layer 3 device."
		},
		{
			"name" : "ip.proto",
			"description" : "Protocol travelling inside IP packet."
		}
	]

