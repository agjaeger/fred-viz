#/usr/bin/python3

import csv
import json

data_dir = 'data/'

raw_files = ['EXPCH.csv', 'EXPGE.csv', 'EXPMX.csv', 'IMPCH.csv', 'IMPGE.csv', 'IMPMX.csv']
output_files = ['zipped.json', 'correlated.json']

data_dict = {}

def writeout(filename, dictionary):
	with open(data_dir + filename, 'w') as data_out:
		json_out = json.dumps(dictionary)
		print(json_out)
	
for data_r in raw_files:
	with open(data_dir + data_r, 'r') as data_read:
		reader = csv.DictReader(data_read)
		columns = reader.fieldnames
			
		for row in reader:
			if row[columns[0]] not in data_dict:
				data_dict[row[columns[0]]] = {}
				
			data_dict[row[columns[0]]][columns[1]] = row[columns[1]]
	
		writeout(output_files[0], data_dict)
	
