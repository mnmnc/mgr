#!/usr/bin/env python3
import protocol

class UDP(protocol.Protocol):
	"""Class for managing wireshark filters for UDP protocol (User Datagram Protocol).

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
		self.name = "UDP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "udp.length", 
			"description" : "Length of datagram."
		},
		{ 
			"name" : "udp.dstport", 
			"description" : "Destination port for datagram."
		},
		{ 
			"name" : "udp.srcport", 
			"description" : "Source port of datagram."
		}
	]









