#/usr/bin/python3

import csv
import json
import itertools
import numpy as np

data_dir = 'data/'

raw_files = ['EXPCH', 'EXPGE', 'EXPMX', 'IMPCH', 'IMPGE', 'IMPMX']

data_dict = {}
correlated_data = {}

def writeout(filename, dictionary):
	json_out = json.dumps(dictionary)
	
	f = open(data_dir + filename, 'w')
	f.write(json_out)
	f.close()
	
def calcCorrelation(key1, key2):
	dataList1 = []
	dataList2 = []
	
	for k, v in data_dict.items():
		dataList1.append(float(data_dict[k][key1]))
		dataList2.append(float(data_dict[k][key2]))

	# correcoef returns 2x2 matrix, row 0 col 1 represents cor(a, b)
	return np.corrcoef(dataList1, dataList2)[0][1]

# read every raw data file
for data_r in raw_files:
	with open(data_dir + data_r + '.csv', 'r') as data_read:
		reader = csv.DictReader(data_read)
		columns = reader.fieldnames
		
		# zip the data together so it is unified
		for row in reader:
			if row[columns[0]] not in data_dict:
				data_dict[row[columns[0]]] = {}
				
			data_dict[row[columns[0]]][columns[1]] = row[columns[1]]
	
		# save the zipped data for future viz
		writeout('zipped.json', data_dict)

# generate a list of perms so i can correlate each one
perms = list(itertools.permutations(raw_files, 2))
for raw in raw_files:
	perms.append([raw, raw])
	
for perm in perms:
	correlated_data[perm[0] + '-' + perm[1]] = calcCorrelation(perm[0], perm[1])

writeout('correlated.json', correlated_data)

