Master 1 Statistique et Informatique Décisionnelle (SID) | Université Toulouse III - Paul Sabatier 
Projet Kaggle - Reddit Score Prediction
Equipe : Team Théo 
@Théo SACCAREAU & @ Théo VEDIS 


**************************************************************************************************************************************************
**************************************************************     ARCHITECTURE     **************************************************************
**************************************************************************************************************************************************

Contenu de l'archive "Team_Theo.zip" : 

	- Le dossier "notebook" contient tous les Notebooks Python qui nous ont permis de mener à bien notre projet : 
		- "(1)_observation_cleaning.ipynb" : Notebook dédié à l'observation et à un premier nettoyage des données  
		- "(2-1)_features_text_1.ipynb" : Notebook dédié à la création de features basées sur l'analyse textuelle
		- "(2-2)_features_text_2.ipynb" : Notebook dédié à la création de features basées sur l'analyse topicale
		- "(2-3)_features_network_1.ipynb" : Notebook dédié à la création de features basées sur le réseau des commentaires/posts
		- "(2-4)_features_network_2.ipynb" : Notebook dédié à la création de features basées sur le réseau des auteurs 
		- "(2-5)_features_others.ipynb" : Notebook dédié à la création de features sur les auteurs, les posts, les dates de publication 
		- "(3)_predictive_model.ipynb" : Notebook dédié à la mise en place d'un modèle de prédiction des scores basé sur les features créées précédemment. 
	
	- Le dossier "scraping" contient les scripts Python et les données qui nous ont permis de récupérer des informations supplémentaires sur le site de Reddit : 
		- deux scripts pythons "authorScrap.py" et "subScrap.py" permettant d'effectuer le scraping 
		- deux fichiers .json "author_id.json" et "post_id.json" permettant aux scripts Python d'aller chercher les bonnes informations
		- deux sous dossiers : 
			- "author" contenant un nouveau script Python "compile.py" qui permet de concaténer les différents "data[1-10].json" en un seul "data.json". 
			En effet, pour gagner du temps nous avons utilisé plusieurs bots de scraping, chacun donnant un fichier .json, nous les regroupons en un seul et même fichier. 
			
			- "post" contient lui aussi un script Python "compile.py" qui a le même objectif de concaténation.  
	(!) Remarque : Ces scripts ne sont pas à ré-exécuter, toutes les données récupérées lors du scraping sont stockées dans deux fichiers .json dans le dossier "data" (voir ci-dessous).  

	- Le dossier 'data' contient 2 fichiers .json contenant les données externes. Ce sont des données que nous avons scrapées sur le site Reddit car nous estimions qu'elles nous aideraient à prédire un commentaire :
		- 'data_author.json' : contient des informations sur les auteurs de commentaires ou de posts : s'ils ont vérifié leur email, leur "comment karma", la date de création de leur compte 
		- 'data_post.json' : contient des informations sur les posts : leur score, leur "up_vote_ratio" (proportion de votes positifs sur proportion de votes totale), leur auteur, leur contenu, leur date de publication. 
	Remarque : Au fur et à mesure des exécutions des différents Notebooks, des fichiers .json et .csv seront créés et stockés dans ce dossier. 


**************************************************************************************************************************************************
**************************************************************   EXECUTION DU CODE   *************************************************************
**************************************************************************************************************************************************

Nous donnerons ci-dessous les instructions permettant de ré-exécuter notre code (et donc notre démarche qui nous a permis d'arriver à notre résultat final). 
Il est essentiel de bien suivre les étapes indiquées afin d'obtenir le même fichier de soumission qui nous a permis d'obtenir le score sur Kaggle. 

* Remarque préliminaire : les instructions ci-dessous sont valables pour l'exécution sur Jupyter Notebook (et non sur Google Collab) à partir de l'architecture de notre archive (chemins relatifs). 
* Comme indiqué précédemment, les scripts concernant le scraping ne sont pas à ré-exécuter. Effectivement, toutes les informations sont déjà stockées dans le dossier "data". 
* Seuls les 7 Notebooks contenus dans le dossier "notebook" sont à re-exécuter. 
* (!) Attention il est obligatoire de respecter l'ordre d'exécution indiqué par les numéros en préfixe : (1) puis (2-1) puis (2-2) puis ... puis (2-5) et enfin (3).  
En effet, lors de l'exécution de chaque Notebook, un fichier est chargé (correspondant au Notebook précédent), modifié puis enregistré (sous un nom différent). 
Ainsi il est obligatoire d'exécuter TOUS les notebooks dans l'ORDRE. 
* Le temps d'exécution de l'ensemble des notebooks est d'environ 2h (le temps d'exécution du Notebook (2-2) exclu car il ne produit aucune feature). 

(0) Pour vous assurez d'avoir l'ensemble des librairies utilisées au cours du projet, nous avons créé un fichier "requirement.txt" contenant l'ensemble de celles-ci.
A l'aide d'un terminal ouvert dans le dossier racine de l'archive, vous pouvez exécuter la commande "pip install -r requirement.txt" pour toutes les installer.
(Nous avons tout de même laisser les commandes "!pip install ..." dans les Notebooks.)

(1) Pour le premier Notebook "(1)_observation_cleaning.ipynb", il est nécessaire de récupérer le Dataset de la compétition Kaggle. Deux solutions sont possibles : 
-> SOIT vous avez déjà le fichier "comments_students.csv" de téléchargé. Dans ce cas, nous vous demandons de :
	- Copier le fichier .csv dans le dossier "data"
	- Ouvrir le Notebook "(1)_observation_cleaning.ipynb" et d'IGNORER (de ne PAS EXECUTER) la partie "Accès à l'API Kaggle avec Jupyter Notebook".
	- Ensuite vous pouvez exécuter l'ensemble de notre code. 
OU 
-> SOIT vous devez exécuter le code au début du Notebook en utilisant l'API Kaggle. Voici comment procéder :
	- Connectez-vous à votre compte Kaggle 
	- Cliquez sur votre profil et rendez-vous à la rubrique "Account" 
	- Dans la zone "API", cliquez sur "Create New API Token". 
	- Enregistrez le fichier "kaggle.json" (par Défaut dans vos paramètres). 
	- Ouvrez le Notebook "(1)_observation_cleaning.ipynb"
	- Suivez les instructions de la partie "Accès à l'API Kaggle avec Jupyter Notebook". 
	- (!) Il est possible que vous ayez besoin de changer le chemin "~/Téléchargements/kaggle.json" en fonction de l'endroit où vous avez téléchargé le fichier "kaggle.json" à l'étape 4. 
	C'est l'unique changement de chemin que vous devrez effectuer. Tous les autres sont des chemins relatifs par rapport à notre architecture d'archive. 
	- Ensuite vous pouvez exécuter l'ensemble de notre code.


(2)  Une fois le premier Notebook exécuté, un fichier "df_clean.json" est créé et stocké dans le dossier "data". C'est le point de départ de notre deuxième Notebbok ("(2-1)_features_text_1.ipynb"). 
Vous devez donc exécuter ce Notebook pour poursuivre notre démarche. Ce deuxième Notebook produira lui-même un nouveau fichier qui sera le point de départ du 4e Notebook. 
Et ainsi de suite jusqu'au dernier Notebook ("(3)_predictive_model.ipynb"). 

(3) Une fois que le dernier Notebook ("(3)_predictive_model") est exécuté, un fichier .csv est créé dans le dossier "data". 
Ce fichier nommé "submission_kaggle.csv" est celui qui doit être utlisé pour la soumission sur le site de Kaggle. 

**************************************************************************************************************************************************
**************************************************************       FEATURES       **************************************************************
**************************************************************************************************************************************************

************************
*** Features "texte" ***
************************
    * Commentaire "robot": 
En regardant les commentaires qui reviennent le plus souvent, nous nous sommes aperçus qu'il y avait des commentaires de type SPAM. Par exemple, le commentaire "Every account on reddit is a bot except you." est présent à 867 reprises. 
Nous avons donc fixé un seuil et une limite de caractères pour déterminer les commentaires "robots" : tous les commentaires qui reviennent plus de 50 fois et qui ont une taille supérieure à 25 caractères seront considérés comme des commentaires "robots". 
La limite sur la taille permet d'éviter de prendre en compte les commentaires du type : "yes", "no", "thanks!", etc, que nous ne considérons pas comme des SPAM. 
L'idée à travers cette feature est que les commentaires identifiés comme "robots" ne devraient pas avoir un score élevé. 

    * Taille du commentaire (en nombre de caractères) avant et après le nettoyage du texte : 
Nous estimons que la taille d'un commentaire est importante. En effet, un commentaire très court (quelques caractères seulement), aura sûrement un score faible alors qu'un commentaire avec une phrase complète aura plus de chance d'avoir un bon score. 
Toutefois, nous pensons que la taille du commentaire ne doit pas être non plus trop grande car sinon les utilisateurs n'auront pas forcément envie de lire un gros paragraphe, et donc le score ne sera pas très élevé. 
Le fait de distinguer la taille avant et après la suppression des stopwords (mots vides) et nettoyage du texte, permet d'avoir une information supplémentaire qui peut nous indiquer la richesse du vocabulaire du commentaire. 
Effectivement, si une phrase avait une longueur assez grande avant le traitement et qu'après sa longueur devient très faible, alors forcément on peut se dire que la richesse du vocabulaire était pauvre (beaucoup de mots vides, etc). 

    * Taille du commentaire (en nombre de mots) après le nettoyage du texte & nombre de mots vides : 
L'intuition est globalement similaire à celle pour la taille en fonction du nombre de caractères. 
Un commentaire qui aura une taille (en termes de nombre de mots) importante après le nettoyage du texte, correspond selon nous a un commentaire avec un vocabulaire assez riche et potentiellement un commentaire qui aura un score plus élevé. 
A l'inverse, un commentaire avec un nombre de mots vides important aura selon nous un score assez faible. 

    * Sentiment du commentaire : 
A partir d'un modèle pré-entrainé, nous avons effectué une analyse de sentiment sur le contenu des commentaires. Cette analyse a permis de déterminer pour chaque commentaire s'il était plutôt "positif", "neutre", "négatif"
Nous estimons que cette information peut être utile pour prédire le score d'un commentaire. 
En effet, un commentaire "positif" aura selon nous plus de chance d'être bien noté. Toutefois, un commentaire "négatif" peut lui aussi être bien noté s'il répond à un sujet/post polémique auquel la majorité des utilisateurs de Reddit ne sont pas d'accord. 
Enfin, un commentaire "neutre" provoque selon nous moins de réaction.

    * Sentiment des enfants : 
En considérant qu'un commentaire positif rapporte +1, qu'un commentaire négatif rapporte -1 et qu'un commentaire neutre rapporte 0, on fait la somme de tous les sentiments des enfants d'un commentaire. Cette somme peut être utile pour prédire un score.
En effet, selon nous, plus cette somme est négative, plus les utilisateurs qui répondent à ce commentaire sont en désaccord et donc plus le commentaire aura tendance à avoir un score faible. 
A l'inverse, un commentaire qui a des enfants majoritairement positifs (en accord avec le commentaire auquel ils répondent), aura un score plus élevé. 

    * Similarité entre le topic/sujet et le commentaire :
Grâce à la métrique "cosinus" nous avons calculé la similarité entre le contenu du sujet/topic et le contenu du commentaire. Plus la similitude est proche, plus le commentaire traite du même sujet que le topic concerné. 
Ainsi, nous estimons que si la similitude est importante, alors le score du commentaire a de bonnes chances d'avoir un score élevé.
Remarque : Nous ne disposions pas du contenu des topics/posts danns notre jeu de données, ce sont donc des informations que nous avons récupérées sur le site Reddit par scraping. 

    * Analyse topicale : 
Initialement, à partir d'une fouille thématique, nous aurions aimé créé une feature renseignant le numéro de cluster pour chaque document et une autre feature renseignant si oui ou non le commentaire appartient au même cluster que son parent. 
Cependant, les résultats du modèle LDA n'étaient clairement pas à la hauteur de nos espérances, nous avons donc fait le choix d'abandonner ces idées de features (cf Notebook "(2-2)_features_text_2.ipynb" pour plus de détails).


*************************
*** Features "réseau" ***
************************* 
  => Réseau n°1 : Ce réseau, basé sur les relations entre commentaires et posts, aura pour noeuds soit des topics (sujets/posts auxquelles font références les commentaires => de type "t3") soit des commentaires (de type "t1"). Les liens seront des relations de parenté. 
   
    * Profondeur d'un commentaire/d'un noeud : 
L'idée de cette feature est de savoir à quelle profondeur le commentaire se trouve, c'est-à-dire, est-ce qu'il répond directement à un topic ou est-ce qu'il répond à un sous-commentaire, lui même sous-commentaire d'un commentaire d'un topic.
Selon nous, plus la profondeur du commentaire est grande, plus le commentaire est difficilement accessible/lisible par les utilisateurs, donc plus son score ne sera pas élevé (visibilité faible).
 
    * Nombre de réponses reçues (directement ou au totale) : 
Ici l'objectif de cette feature est de connaitre le nombre de réponses reçues par un commentaire (directement ou au total, c'est-à-dire, en comptant les sous-réponses).
Pour nous, plus un commentaire a fait réagir, plus il a été vu, et potentiellement, plus son score peut-être élevé (visibilité élevée).


  => Réseau n°2 : Ce réseau, axé sur les auteurs, aura donc pour noeuds l'ensemble des auteurs de notre jeu de données. Si un auteur répond à un commentaire d'un autre auteur, alors cette relation est matérialisée par une arête (dirigée dans le sens auteur qui répond vers l'autre auteur). 

    * Centralité : 
Dans un réseau (normalement plutôt non-dirigé mais fonctionne sur les réseaux dirigés également), la centralité d'un noeud est liée à son implication avec d'autres noeuds et sa participation dans de nombreux liens. 
Peu importe si la proéminence est due à la réception ou à la transmission de nombreux liens.
Il existe plusieurs métriques permettant de mesurer la centralité, mais pour toutes, l'objectif est de mesurer à quel point un noeud est impliqué dans le réseau, à quel point il est central. Intuitivement, plus l'acteur est connecté plus la centralité sera importante.
Dans notre projet, plus la centralité de l'auteur d'un commentaire sera importante, plus son score a de bonnes chances (selon nous) d'être élevé car l'auteur étant au centre du réseau, son commentaire aura une plus forte visibilité qu'un commentaire ayant un auteur en périphérie.

        - Centralité degré :
La première métrique est calculée à partir du degré d'un auteur. On ne distingue pas les degrés entrants (commentaires reçus pour un auteur) ou sortants (commentaires émis par un auteur). 
Interprétation :
    Valeur élevée : contact direct avec de nombreux autres auteurs (=> scores plus élevés ?)
    Valeur faible : pas actif, auteur périphérique (=> scores plus faibles ?) 

        - Centralité liée aux vecteurs propres :
Pour cette métrique, l'idée est que l'importance d'un noeud dépend de l'importance de ses voisins (définition récursive).
Remarque : Bien que généralement les différentes métriques de centralité sont corrélées positivement (quand ce n'est pas le cas cela met en évidence des noeuds caractéristiques), nous avons fait le choix , à ce stade, d'en garder plusieurs. 
C'est lors de l'apprentissage du modèle prédictif et surtout son amélioration que nous supprimerons peut être quelqu'unes de ces métriques.

        - Intermédiarité et proximité :
Nous aurions aimé calculer ces deux autres métriques vues en cours. Cependant, le graphe étant tellement important (2millions de relations) qu'après une nuit d'exécution, l'algortihme n'était toujours pas fini (arrêté au bout de 18h). 
Nous n'aurons donc pas de features liées à la centralité intermédiaire ou proximité. 

    * Prestige d'un noeud :
Comme pour la centralité, son objectif est de mesurer l'importance d'un noeud dans un réseau. Cependant, il est un peu plus subtil que cette dernière puisqu'il distingue les relations entrantes des relations sortantes (il se calcule uniquement sur les graphes dirigés donc). 
Un noeud prestigieux est un noeud souvent référencé (dans notre cas un auteur qui reçoit beaucoup de commentaires).
Une fois de plus, plusieurs métriques sont possibles.

        - Prestige - degré :
Comme pour la centralité, la première métrique est liée au degré d'un noeud, sauf qu'ici on ne considère que les noeuds entrants. 

        - Autre prestige :
Comme pour la centralité, les autres métriques prennent trop de temps à être calculées. Nous nous contenterons uniquement du prestige degré.
De plus, la librairie 'networkw' n'a pas de fonction qui permet de calculer directement ces autres métriques, ainsi si nous le faisions à la main, les fonctions seraient encore moins optimisées et prendraient énormément de temps. 

    * Communautés : 
A travers ce réseau, l'extraction de communautés semblait être pertinente. Nous pensions que détecter des groupes d'auteurs qui intéragissent souvent ensemble (et rarement avec d'autres auteurs ne faisant pas partie de leur communauté), 
pouvait être un indicateur permettant de prédire le score d'un commentaire.
Nous avons essayé une grande partie des algorithmes implémentés dans la librairie NetworkX, des algortihmes vus en cours (Clique Percolation), manipulés en TP (Girvan Newman, bipartition de Kernighan–Lin, Fluid communities algorithm), 
ou même de nouveaux algorithmes (Naive Greddy Modularity, Label propagation, etc). 
Cependant, une fois de plus, à cause de l'importance du nombre de noeuds, une grande majorité des algorithmes mettaient trop de temps à s'exécuter. 
L'inconvénient des méthodes implémentées dans les librairies est que nous ne savions pas le temps d'exécution restant (au contraire de nos méthodes en utilisant le TQDM). 
Ainsi, après quelques heures d'exécution, nous interrompions l'exécution sans savoir si elle allait se terminer dans 5h ou 5min...

L'un des deux seuls algorithmes qui nous a donné des résultats était la bipartition de Kernighan–Lin. Comme son nom l'indique, cet algortihme permet de séparer le réseau en deux. 
Ici, étant donné que le réseau était consitué de 500 000 auteurs, le séparer seulement en deux nous semblait être un peu juste pour que cela nous aide à prédire le score d'un commentaire. 
De plus, les métriques évaluant la qualité de ce partitionnement nous indiquaient que la répartition n'était pas bonne. Nous avons décidé de ne pas en faire une feature. 

L'autre algorithme qui fonctionnait, était CPM (Clique Percolation Method).Cependant, nous n'avons pas créé une feature à partir de lui pour plusieurs raisons. 
Tout d'abord, comme c'est un algorithme qui permet de détecter des communautés qui se chevauchent (un auteur peut appartenir à plusieurs communautés ou à aucune), son résultat n'est pas une partition. 
Ainsi, les métriques permettant d'évaluer la qualité d'un partitionnement (modularité, couverture, performance) ne fonctionnent pas. 
Il était donc difficile de savoir si les communautés extraites étaient de bonne qualité ou pas, et surtout, il était impossible de mesurer s'il était mieux de prendre k=3, k=4, k5, ou plus.
De plus, peu d'acteurs étaient finalement concernés par l'extraction de communautés via la méthode de percolation (la majorité n'appartenait à aucune communauté). 
On avait donc peu d'auteurs présents dans un grand nombre de communautés qui étaient majoritairement composées que de quelques auteurs. 
Ainsi, nous estimions que cette information ne serait clairement pas utile pour prédire le score d'un commentaire, nous avons donc décider de ne pas en faire une feature. 

*************************
*** Features "autres" ***
*************************
Nous avons créé également d'autres features pour prédire le score d'un commentaire mais qui ne correspondaient pas à des features liées au texte ou aux réseaux.

Remaque : Plusieurs features ci-dessous ont nécessité des informations que nous ne disposions pas dans notre jeu de données et que nous avons donc scrapées. 
Les informations scrapées portaient : 
   - sur les auteurs : s'il a vérifié son email, son "comment karma", la date de création de son compte 
   - sur les posts : leur score, leur "up_vote_ratio" (proportion de votes positifs sur proportion de la totalité des votes), leur auteur, leur contenu, leur date de publication. 

    * Features sur les dates : 
	- Moment de la journée où le commentaire a été publié : 
Nous estimons que l'heure d'un commentaire peut avoir une influence sur le score obtenu.
Effectivement, il y a certain moment de la journée où il y a moins d'utilisateurs connectés à Reddit (et lorsque l'affluence est de nouveau importante, le commentaire se retrouve en bas d'une discussion ou est moins visible).
La visibilité du commentaire est donc moins importante, ce qui peut impacter négativement son score.  

	- Temps de réponse commentaire-parent
Cette nouvelle variable nous permet de connaitre le temps de réponse d'un commentaire vis à vis de son parent. 
Pour nous, plus le temps de réponse est important plus le score risque d'être faible. En effet, un commentaire qui répond à un commentaire datant de plusieurs jours, aura forcément moins de visibilité qu'un commentaire qui a répondu immédiatement. 

	- Temps de réponse commentaire-topic
Quasiment identique à la feature précédente sauf qu'ici on regarde le temps de réponse entre le commentaire et le sujet (et non le parent). 
Dans certains cas, les deux informations peuvent être identiques (si le commentaire est directement une réponse à un topic), mais d'en d'autres situations ce sera une information complémentaire. 
Comme précédemment, nous estimons que plus le temps de réponse est important plus le score risque d'être faible. En effet, un commentaire qui répond à un sujet datant de plusieurs jours, aura forcément moins de visibilité qu'un commentaire qui a répondu immédiatement. 

    * Features sur la polarité du sujet : 
	- Score du parent / score du topic :
Le fait de connaitre cette information peut aider, selon nous, à prédire le score d'un commentaire. 
Effectivement, si le topic et/ou le parent de notre commentaire ont un score important, notre commentaire a plus de chance d'avoir un score plus élevé qu'un commentaire qui a un topic et son parent avec un petit score.
Bien évidemment, il peut y avoir des exceptions, par exemple, un commentaire qui répond à un sujet polémique (ayant reçu majoritairement des unlikes plutôt que des likes) et qui le contredit se verra recevoir beaucoup de "likes" de la part des utilisateurs qui ne sont pas d'accord avec le post initial.
Remarque : Si le parent du commentaire est un topic (t3) alors les deux variables seront identiques dans ce cas. 


	- Nombre de commentaires pour le topic / Nombre de commentaires pour le parent
Cette feature peut être vue de façon différente pour son aide à prédire un score.
En effet, on peut se dire que plus le nombre de commentaires est élevé pour le topic et/ou le parent, plus notre commentaire va se noyer dans la masse de commentaires, et donc difficilement recevoir des likes. Ainsi, plus cette variable serait élevée, plus le score serait faible.
Cependant, on peut voir la situation d'une autre façon. On peut effectivement considérer que plus le nombre de commentaires est élevé, plus c'est un sujet populaire et donc plus l'audience est élevée. 
Ce qui signifierait que plus il y a de commentaires, plus notre commentaire a de chance d'avoir plein de likes et donc un score important.
Remarques :
    Ici on souhaite avoir le nombre de commentaires directs.
    Si le parent du commentaire est un topic (t3) alors les deux variables seront identiques.

	- Rapport du nombre de votes positifs sur le nombre de la totalité des votes pour un sujet/post :
Pour cette dernière feature, nous utilisons directement l'information scrapée sur Reddit.
Pour nous, connaitre le rapport nombre de votes positifs reçus sur nombre de la totalité des votes pour un sujet est un indicateur sur sa popularité.
Pour nous un post qui a un ratio de 1 (qui n'a reçu que des likes et pas de dislikes), est un post apprécié et donc potentiellement ses commentaires le seront aussi. 

    * Features sur les auteurs
	- Score moyen de l'auteur
Le fait d'avoir le score moyen d'un auteur est bien évidement déterminant dans la prédiction du score d'un de ces nouveaux commentaires. 
Si en général, il obtient des scores élevés, c'est qu'il donne des avis/commentaires pertinents et appréciés par une partie des utilisateurs de Reddit. Ainsi, pour tout nouveau commentaire, il y a plus de chance qu'il obtienne un bon score qu'un auteur qui obtient d'habitude de mauvais scores. 

	- Même auteur que le topic
Pour nous, si l'auteur d'un commentaire est le même que l'auteur du topic initial, il y a de bonne chance que le commentaire est un bon score (car il peut apporter une précision, un complément d'informations, etc).
Ce n'est qu'une hypothèse, nous verons lors de l'apprentissage du modèle si cette feature est importante ou pas.
Ce sera donc une variable binaire avec 0 si l'auteur du commentaire est différent de l'auteur du topic, 1 si ce sont les mêmes. 

	- Année de création de son compte 
L'année de création du compte de l'auteur peut éventuellement être une information permettant de déterminer le score de son commentaire. 
Nous estimons en effet que plus l'auteur est inscrit depuis longtemps, plus il comprend le fonctionnement de Reddit et des astuces pour avoir plus de votes positifs. 

	- Vérification du compte 
Le fait de savoir si l'auteur a vérifié son email peut nous aider à prédire le score puisque nous pensons que les auteurs qui ne l'ont pas fait sont soit des auteurs "robots" soit des auteurs qui peuvent potentiellement mettre des commentaires polémiques, insultants, etc (et donc avoir des scores faibles).

	- Comment karma 
Enfin, la dernière feature mise au point est le "comment karma" d'un auteur.  Le comment karma est une métrique utilisée par Reddit qui correspond à la somme des scores reçus par un auteur.
Ainsi, plus cette métrique est importante, plus l'auteur a reçu de likes depuis la création de son compte. Il donne alors des avis/commentaires pertinents et appréciés par une partie des utilisateurs de Reddit.
Pour tout nouveau commentaire, il y a donc plus de chance qu'il obtienne un bon score qu'un auteur a un comment karma faible. 
Remarque : Cette feature peut sembler redondante avec la moyenne des scores des auteurs, sauf qu'ici le comment karma concerne les scores sur toute période alors que la moyenne des scores des auteurs est basée sur les scores de notre jeu de données, c'est-à-dire sur les scores obtenues en Mai 2015 seulement.   
