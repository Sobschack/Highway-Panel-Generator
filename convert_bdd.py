import os
import csv
import json
import random
import time
from constant import field_index

start = time.time()

csv_data = "data/villes_france.csv"
json_data = "data/villes_france.json"
my_path = os.path.realpath(__file__)
cwd = os.path.dirname(my_path)
csv_file = os.path.join(cwd, csv_data)
json_file = os.path.join(cwd, json_data)

my_dict = {}

with open(csv_file, "r") as link :
    contenu = csv.reader(link, delimiter=",")
    for row in contenu:
        # test = row[field_index["ville_id"]]
        my_dict[row[field_index["ville_id"]]] =  row[1:]
        
with open (json_file, "w") as json_link:
    json.dump(my_dict, json_link)
    print("Json file created")

# for i in range(3):
#     my_rand = str(random.randint(0, len(my_dict)))
#     print(my_dict[my_rand][(field_index["ville_nom"])])

stop = time.time()
print(stop-start)