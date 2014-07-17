#!/usr/bin/env python3
import protocols.protocol as protocol

class DNS(protocol.Protocol):
	"""Class for managing wireshark filters for DNS protocol (Domain Name System).

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
		self.name = "DNS"
		self.fields_selected = []


	fields_available = [
		{ 
			"name" : "dns.id", 
			"description" : "Identification number of request/response"
		},
		{ 
			"name" : "dns.qry.name", 
			"description" : "Name that is queried."
		},
		{ 
			"name" : "dns.qry.type", 
			"description" : "Type of query. NS | A | IN | PTR | MX | SOA | AXFR"
		},
		{ 
			"name" : "dns.resp.addr", 
			"description" : "Resolved address."
		},
		{ 
			"name" : "dns.resp.type", 
			"description" : "NS | A | IN | PTR | MX | SOA | AXFR"
		},
		{ 
			"name" : "dns.count.answers", 
			"description" : "Number of addresses returned by the server."
		},
		{ 
			"name" : "dns.ptr.domain_name", 
			"description" : "In case of an alias/ptr - what is the name translates to."
		}
	]










