#!/usr/bin/env python3
import pprint

class Protocol:
	"""BASE CLASS FOR OTHER PROTOCOLS"""

	fields_available = []
	

	def __init__(self):
		self.name = "Protocol"
		self.fields_selected = []

	def print(self, switch):
		"""Prints fields as lists."""

		pp = pprint.PrettyPrinter(indent=4)
		if switch == "all":
			pp.pprint(self.fields_available)
		elif switch == "sel":
			pp.pprint(self.fields_selected)
		elif switch == "nsel":
			print(self.name)
			pp.pprint(self.fields_selected)
		elif switch == "nall":
			print(self.name)
			pp.pprint(self.fields_available)
		else :
			pp.pprint("UKNOWN PARAMETER")



	def select_field(self, name):
		"""Adds field specified by name, to list of selected ones."""

		for field in self.fields_available:
			if field["name"] == name:
				self.fields_selected.append(field)

	def select_all(self):
		""""Adds all available fields to selected list."""

		for field in self.fields_available:
			self.select_field(field["name"])

	def remove_all(self):
		"""Removes all fields from selected list."""

		for field in self.fields_selected:
			self.remove_field(field["name"])

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

