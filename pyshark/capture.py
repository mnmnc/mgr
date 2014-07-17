#!/usr/bin/env python3
import protocol

class DNS(protocol.Protocol):
	"""Class for managing wireshark filters for DNS protocol (Domain Name System).

	Dependencies:
		Protocol class needs to be imported.

	Properties:
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

	fields_selected = []

	def print(self, switch):
		"""Prints fields as lists."""

		if switch == "all":
			print(self.fields_available)
		elif switch == "sel":
			print(self.fields_selected)
		else :
			print("UKNOWN PARAMETER")

	def select_field(self, name):
		"""Adds field specified by name, to list of selected ones."""

		for field in self.fields_available:
			if field["name"] == name:
				self.fields_selected.append(field)

	def remove_field(self, name):
		"""Removes field specified by name, from a list of selected ones."""

		position = 0
		popped = None
		for field in self.fields_selected:
			if field["name"] == name:
				popped = self.fields_selected.pop(position)
			position = position + 1
		return popped

	def print_description(self, name):
		"""Prints description of the field selected by name."""

		for field in self.fields_available:
			if field["name"] == name:
				print(field["description"])

	def get_description(self, name):
		"""Returns description of selected field as string."""

		for field in self.fields_available:
			if field["name"] == name:
				return field["description"]

	def get_names_available(self):
		"""Returns a list of names of available fields"""

		_list = []
		for field in self.fields_available:
			_list.append(field["name"])
		return _list

	def get_names_selected(self):
		"""Returns a list of names of selected fields"""

		_list = []
		for field in self.fields_selected:
			_list.append(field["name"])
		return _list




# dns.id
# dns.qry.name
# dns.qry.type
# dns.resp.addr
# dns.resp.type
# dns.count.answers
# dns.ptr.domain_name










