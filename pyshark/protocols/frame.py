#!/usr/bin/env python3
import protocols.protocol as protocol

class Frame(protocol.Protocol):
	"""Class for managing wireshark filters for lowest layer of network communication

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
		self.name = "Frame"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "frame.time_epoch", 
			"description" : "Time of frame arival. Example: 1405588103.287104000"
		},
		{
			"name" : "frame.protocols",
			"description" : "Protocols traveling within selected frame. Example: eth:ip:icmp"
		}
	]






