"""Documentation
Date: Lundi 5 avril 2021

Compétition Kaggle - Team Théo

@auteur: Théo SACCAREAU & Théo VEDIS

authorScrap.py

Description: Dans ce fichier Python, nous nous intéressons à la collecte des informations des différents autheurs
comme leur comment-karma, est-ce que leur email est vérifié et leur date de création de compte.

Commande de lancement: python3.8 authorScrap.py [Numero du bot] [Nombre de ligne]
    - Numéro du bot : un numéro entre 1 et ∞
    - Nombre de lignes : nombre de ligne que le bot va collecter

ex : python3.8 authorScrap.py 1 60.000

Idée: Diviser la tâche en plusieurs programmes en parallèle pour aller plus vite!
    Soit lancer 10 bot avec 60.000 lignes chacun (570.000 auteurs au total).
"""


import praw
from tqdm import tqdm
import json
import sys

# Chemin vers le fichier contenant la liste des Id des topics
pathFile = r"\author_id.json"

# Initialisation de l'API reddit
CLIENT_ID = "muixdGPDu0ShZw"
SECRET_KEY = "z0xR7dHrRV40nqdTqhNzROSa5bt6ng"
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET_KEY, user_agent="BOT")
reddit.read_only = True

# Argument pour diviser la tache en plusieur scrapper
bot_num = int(sys.argv[1])
size = int(sys.argv[2])

# Chargement des Id des post
with open(pathFile, "r") as f:
    data = json.load(f)

# Début du scraping
author_info = {}
for i in tqdm(
    range(len(data[(bot_num - 1) * size : min(len(data), bot_num * size)])),
    total=min(len(data) - (bot_num - 1) * size, size),
):
    i += (bot_num - 1) * size
    try:
        redditor: praw.models.reddit.redditor.Redditor = reddit.redditor(data[i])
        author_info[data[i]] = {}
        try:
            author_info[data[i]]["has_verified_email"] = bool(
                redditor.has_verified_email
            )
        except:
            author_info[data[i]]["has_verified_email"] = None

        try:
            author_info[data[i]]["comment_karma"] = int(redditor.comment_karma)
        except:
            author_info[data[i]]["comment_karma"] = None

        try:
            author_info[data[i]]["time"] = int(redditor.created_utc)
        except:
            author_info[data[i]]["time"] = None

    except:
        pass


# Ecriture du fichier avec les nouvelles données collectées
with open("./data" + str(bot_num) + ".json", "w+") as f:
    json.dump(author_info, f)
