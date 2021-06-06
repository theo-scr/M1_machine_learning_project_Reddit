"""Documentation
Date: lundi 5 avril 2021

Compétition Kaggle - Team Théo

@auteur: Théo SACCAREAU & Théo VEDIS

compile.py

Description: Ce fichier a pour but de concaténer les différents data[1-10].json en un seul data.json
"""

from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import json

mypath = r"./"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

data = {}
for i in tqdm(onlyfiles):
    if ".json" in i:
        with open(mypath + i, "r") as f:
            sub_data = json.load(f)
            data.update(sub_data)

with open(mypath + "data.json", "w") as f:
    json.dump(data, f)
