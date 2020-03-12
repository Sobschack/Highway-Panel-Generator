import os
import csv
from constant import field_index

csv_data = "data/villes_france.csv"
my_path = os.path.realpath(__file__)
cwd = os.path.dirname(my_path)
csv_file = os.path.join(cwd, csv_data)

with open(csv_file, "r") as link :
    contenu = csv.reader(link, delimiter=",")
    for row in contenu:
        print(row[field_index["ville_id"]])
        print(row[field_index["ville_nom"]])
print(type(row))
