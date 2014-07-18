#!/usr/bin/env python3

import protocols.protocol as protocol
from protocols import frame, ethernet, arp, ip, tcp, udp, http, dns

class Protocols_list:
	"""Manages the list of protocols.

	Dependencies:
		protocols.protocols_list
		frame, ethernet, arp, ip, tcp, udp, http, dns

	Functions:
		select_all
		remove_all
		remove_protocol
		print_protocols
	"""
	def __init__(self):
		
		self.ip 	= ip.IP()
		self.arp 	= arp.ARP()
		self.tcp 	= tcp.TCP()
		self.udp 	= udp.UDP()
		self.dns 	= dns.DNS()
		self.http 	= http.HTTP()
		self.frame 	= frame.Frame()
		self.eth 	= ethernet.Ethernet()

		self.protocols_list = [self.frame, self.eth, self.arp, self.ip, self.tcp, self.udp, self.http, self.dns]

	def select_all(self):
		"""Selects all fields in protocols."""

		for proto in self.protocols_list:
			proto.select_all()

	def remove_all(self):
		"""Removes all fields in protcols."""

		for proto in self.protocols_list:
			proto.remove_all()

	def remove_protocol(self, protocol_name ):
		"""Removes specified protocol from protocols_list."""

		for proto in self.protocols_list:
			if protocol_name.lower() == (type(proto).__name__).lower():
				self.protocols_list.pop(self.protocols_list.index(proto))
				print("Removed", type(proto).__name__)

	def print_protocols(self):
		"""Lists protocols names."""

		for proto in self.protocols_list:
			print( type(proto).__name__ )

	def create_name_list(self):
		"""Creates list of selected fields within protocols."""

		self.result_list = []
		for proto in self.protocols_list:
			temp_list = proto.get_names_selected()
			for item in temp_list:
				self.result_list.append(item)

	def param_string_from_list(self, param_prefix ):
		"""Concatenates the list of selected fileds with specified prefix."""

		self.param_string = ""
		for item in self.result_list:
			self.param_string = self.param_string + " " + param_prefix + " " + item 

	def print_param_string(self):
		"""Prints parameter string."""
		print(self.param_string)

	def print_param_string(self):
		"""Returns parameter string."""
		return self.param_string

proto_list = Protocols_list()
proto_list.select_all()
proto_list.print_protocols()

proto_list.print_protocols()
proto_list.create_name_list()
proto_list.param_string_from_list("-e")
proto_list.print_param_string()
