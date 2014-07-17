#!/usr/bin/env python3
import protocol

class TCP(protocol.Protocol):
	"""Class for managing wireshark filters for TCP protocol (Transmission Control Protocol).

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
		self.name = "TCP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "tcp.dstport", 
			"description" : "Destination port of segment."
		},
		{ 
			"name" : "tcp.srcport", 
			"description" : "Source port of segment."
		},
		{ 
			"name" : "tcp.seq", 
			"description" : "Sequence number of segment."
		},
		{ 
			"name" : "tcp.ack", 
			"description" : "Number of segment that has been delivered."
		},
		{ 
			"name" : "tcp.flags.fin", 
			"description" : "Flag used in graceful connection termination."
		},
		{ 
			"name" : "tcp.flags.ack", 
			"description" : "Acknowledgement flag."
		},
		{ 
			"name" : "tcp.flags.syn", 
			"description" : "Synchronization flag. Used in first segment to start the connection."
		},
		{ 
			"name" : "tcp.flags.reset", 
			"description" : "Flag responsible for abrupt connection termination."
		},
		{ 
			"name" : "tcp.flags.push", 
			"description" : "Flag used when segment contains data for higher layers."
		},
		{ 
			"name" : "tcp.flags.ns", 
			"description" : "Nonce sum. Single-bit sum of ECN fields values. Used for integrity verification."
		},
		{ 
			"name" : "tcp.flags.cwr", 
			"description" : "Congestion window reduced flag. Response informing that host received echo request and this can stop now."
		},
		{ 
			"name" : "tcp.flags.ecn", 
			"description" : "Flag set after receiving packet with CE flag."
		},
		{ 
			"name" : "tcp.flags.res", 
			"description" : "Reserved bits."
		},
		{ 
			"name" : "tcp.flags.urg", 
			"description" : "Urgency flag. Informs about importance of priority field."
		},
		{ 
			"name" : "tcp.analysis.bytes_in_flight", 
			"description" : "Number of Bytes of data travelling in this segment."
		}

	]

	









