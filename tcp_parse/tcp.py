
import csv

def make_packet(packet_data):
	return { "id": packet_data[0],
			"time" : packet_data[1],
			"len" : packet_data[2],
			"src" : packet_data[3],
			"dst" : packet_data[4],
			"sport" : packet_data[5],
			"deport" : packet_data[6],
			"ttl" : packet_data[7],
			"flags" : packet_data[8]
	}

def print_data(data):
	for i in range(len(data)):
			print(data[i])

def set_header(head):
	result = []
	for i in range(len(head)):
		result.append(head[i])
	return result

def parse_file(local_file):
	data = []
	headers = []
	with open(local_file) as input_file:
		# READ CSV
		csv_file = csv.reader(input_file)

		header_loaded = False
		for row in csv_file:
			if not header_loaded:
				# IF THIS IS HEADER
				headers = set_header(row)
				header_loaded = True
			else:
				data.append(make_packet(row))

	return headers, data

def get_unique_values(data, attribute):
	result = set([])
	for packet in data:
		result.add(packet[attribute])
	return result

def count_values_for_attribute_value(data, attribute, value):
	result = 0
	for packet in data:
		if packet[attribute] == value:
			result+=1
	return result

def ip_to_decimal(ip):
	ip_arr = ip.split(".")
	return int(ip_arr[0]) * 256 * 256 * 256 + int(ip_arr[1]) * 256 * 256 + int(ip_arr[2]) * 256 + int(ip_arr[3])

def ip_xor(ip_1, ip_2):
	return ip_to_decimal(ip_1) ^ ip_to_decimal(ip_2)

def get_list_2_attr(data, attribute_1, attribute_2):
	result = []
	for packet in data:
		result.append([packet[attribute_1], packet[attribute_2]])
	return result

def xor_all_pairs(pairs_list):
	result = []
	for pair in pairs_list:
		result.append([pair[0], pair[1], ip_xor(pair[0], pair[1])])
	return result

def print_list_of_lists(list_of_lists):
	for inner_list in list_of_lists:
		print(inner_list)

def convert_data_to_numeric(data):
	for packet in data:
		src = packet["src"]
		dst = packet["dst"]
		deport = packet["deport"]


def main():
	data = []
	input_data_file = "data.csv"
	headers, data = parse_file(input_data_file)

	ttl_set = (get_unique_values(data, "sport"))

	print_data(data)
	# for value in sorted(ttl_set, key=lambda val: int(val)):
	# 	print("sport value:",value, "count:", count_values_for_attribute_value(data,"sport", value))

	#pair_list = get_list_2_attr(data, "src", "dst")
	#xored = xor_all_pairs(pair_list)
	#print_list_of_lists(xored)


if __name__ == "__main__":
	main()