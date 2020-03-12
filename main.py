import os
import csv

csv_data = "data/villes_france.csv"
my_path = os.path.realpath(__file__)
cwd = os.path.dirname(my_path)
csv_file = os.path.join(cwd, csv_data)

field_index = {
    "ville_id" : 0,
    "ville_departement" : 1,
    "ville_slug" : 2,
    "ville_nom" : 3,
    "ville_nom_simple" : 4,
    "ville_nom_reel" : 5,
    "ville_nom_soundex" : 6,
    "ville_nom_metaphone" : 7,
    "ville_code_postal" : 8,
    "ville_commune" : 9,
    "ville_code_commune" : 10,
    "ville_arrondissement" : 11,
    "ville_canton" : 12,
    "ville_amdi" : 13,
    "ville_population_2010" : 14,
    "ville_population_1999" : 15,
    "ville_population_2012" : 16,
    "ville_densite_2010" : 17,
    "ville_surface" : 18,
    "ville_longitude_deg" : 19,
    "ville_latitude_deg" : 20,
    "ville_longitude_grd" : 21,
    "ville_latitude_grd" : 22,
    "ville_longitude_dms" : 23,
    "ville_latitude_dms" : 24,
    "ville_zmin" : 25,
    "ville_zmax" : 26,
}

with open(csv_file, "r") as link :
    contenu = csv.reader(link, delimiter=",")
    for row in contenu:
        print(row[field_index["ville_id"]])
        print(row[field_index["ville_nom"]])
print(type(row))
