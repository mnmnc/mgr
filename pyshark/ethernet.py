#!/usr/bin/env python3
import protocol

class Ethernet(protocol.Protocol):
	"""Class for managing wireshark filters for Ethernet protocol (IEEE 802.3).

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
		self.name = "Ethernet"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "eth.dst", 
			"description" : "MAC address of destination."
		},
		{
			"name" : "eth.src",
			"description" : "MAC address of source."
		},
		{
			"name" : "eth.lg",
			"description" : "Whether the MAC address is globally unical."
		},
		{
			"name" : "eth.ig",
			"description" : "Whether this a unicast or broadcast."
		}
	]









