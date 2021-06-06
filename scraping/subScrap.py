"""Documentation
Date: Lundi 5 avril 2021

Compétition Kaggle - Team Théo

@auteur: Théo SACCAREAU & Théo VEDIS

subScrap.py

Description: Dans ce fichier Python, nous nous intéressons à la collecte des informations des différents topics
comme leur score, leur ratio de votes positifs, le nom de l'auteur, leur titre (contenu), et leur date de publication.

Commande de lancement: python3.8 subScrap.py [Numero du bot] [Nombre de ligne]
    - Numéro du bot : un numéro entre 1 et ∞
    - Nombre de lignes : nombre de ligne que le bot va collecter

ex : python3.8 subScrap.py 1 15.000

Idée: Diviser la tâche en plusieurs programmes en parallèle pour aller plus vite!
    Soit lancer 10 bot avec 15.000 lignes chacun (148.000 topics au total)

"""

import praw
from tqdm import tqdm
import json
import sys

# Chemin vers le fichier contenant la liste des Id des topics
pathFile = r"post_id.json"

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

# Debut du scrapping
sub_info = {}
for i in tqdm(range(len(data)), total=min(len(data) - bot_num * size, size)):
    if i >= (bot_num - 1) * size and i < (bot_num) * size:
        sub: praw.models.reddit.submission.Submission = reddit.submission(data[i][3:])

        sub_info[data[i]] = {}
        sub_info[data[i]]["score"] = int(sub.score)
        sub_info[data[i]]["up_vote_ratio"] = float(sub.upvote_ratio)
        sub_info[data[i]]["author"] = str(sub.author)
        sub_info[data[i]]["title"] = str(sub.title)
        sub_info[data[i]]["time"] = int(sub.created_utc)


# Ecriture du fichier avec les nouvelles données collectées
with open("./data" + str(bot_num) + ".json", "w+") as f:
    json.dump(sub_info, f)
