#!/usr/bin/env python3
import protocol

class ICMP(protocol.Protocol):
	"""Class for managing wireshark filters for ICMP protocol (Internet Control Message Protocol).

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
		self.name = "ICMP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "icmp.type", 
			"description" : "8 -> echo request, 0 -> echo reply, 3 -> destination unreachable, 11 -> TTL exceeded"
		},
		{
			"name" : "icmp.code",
			"description" : "3 -> port unreachable"
		},
		{
			"name" : "icmp.seq",
			"description" : "Sequence identification number (BigEndian). Allows to connect request and response."
		}
	]

	


