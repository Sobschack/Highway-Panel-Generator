import os
import json
import random
import time
from constant import field_index


def read(path):
	with open (path, "r") as f:
		data = json.load(f)
	return data

def display(data):
	keys = list(data.keys())
	random.shuffle(keys)
	for i in range(3):
	    key = keys[i]
	    print(data[key]["ville_nom"])

size = max(5, len(nom))

if __name__=="__main__":
	json_data = "data/villes_france_2.json"
	my_path = os.path.realpath(__file__)
	cwd = os.path.dirname(my_path)
	json_file = os.path.join(cwd, json_data)

	start = time.time()

	my_dict = read(json_file)
	display(my_dict)

	stop = time.time()
	print(stop-start)