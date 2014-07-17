#!/usr/bin/env python3
import protocol

class HTTP(protocol.Protocol):
	"""Class for managing wireshark filters for HTTP protocol (Hyper Text Transfer Protocol).

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
		self.name = "HTTP"
		self.fields_selected = []

	fields_available = [
		{ 
			"name" : "http.request.method", 
			"description" : "GET | HEAD | POST | PUT | DELETE | TRACE | CONNECT "
		},
		{ 
			"name" : "http.request.uri", 
			"description" : "Path to requested resource."
		},
		{ 
			"name" : "http.request.version", 
			"description" : "Whether this is HTTP/1.0  or HTTP/1.1."
		},
		{ 
			"name" : "http.host", 
			"description" : "Domain."
		},
		{ 
			"name" : "http.response.code", 
			"description" : "2** - Document | 3** - Cache/Redirect | 4** Document not available | 5** Server error "
		},
		{ 
			"name" : "http.response.phrase", 
			"description" : "For example <Not Found> when 404 is the response code."
		},
		{ 
			"name" : "http.server", 
			"description" : "Server name that handled the request."
		},
		{ 
			"name" : "http.content_length_header", 
			"description" : "Length of data send in response or request."
		},
		{ 
			"name" : "http.referer", 
			"description" : "Where from the request is comming from."
		}
	]










