import os
import csv
import json
import random
import time
from constant import field_index

start = time.time()

csv_data = "data/villes_france.csv"
json_data = "data/villes_france_2.json"
my_path = os.path.realpath(__file__)
cwd = os.path.dirname(my_path)
csv_file = os.path.join(cwd, csv_data)
json_file = os.path.join(cwd, json_data)

my_dict = {}

names = [	"ville_departement",
		    "ville_slug",
		    "ville_nom",
		    "ville_nom_simple",
		    "ville_nom_reel",
		    "ville_nom_soundex",
		    "ville_nom_metaphone",
		    "ville_code_postal",
		    "ville_commune",
		    "ville_code_commune",
		    "ville_arrondissement",
		    "ville_canton",
		    "ville_amdi",
		    "ville_population_2010",
		    "ville_population_1999",
		    "ville_population_2012",
		    "ville_densite_2010",
		    "ville_surface",
		    "ville_longitude_deg",
		    "ville_latitude_deg",
		    "ville_longitude_grd",
		    "ville_latitude_grd",
		    "ville_longitude_dms",
		    "ville_latitude_dms",
		    "ville_zmin",
		    "ville_zmax"]

with open(csv_file, "r") as link :
    contenu = csv.reader(link, delimiter=",")
    for row in contenu:
        key_id = row[field_index["ville_id"]]
        data = {}
        liste = row[1:]
        for i in range(len(liste)):
        	data[names[i]] = liste[i]
        my_dict[int(key_id)] = data
        
with open (json_file, "w") as json_link:
    json.dump(my_dict, json_link, indent=4)
    print("Json file created")

stop = time.time()
print(stop-start)