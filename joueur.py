"""
Classe Joueur, le joueur aura 8 attributs :
I) Construction
** Données :
1) Nom : Le nom du joueur
2) Couelur : La couleur du joueur

** Générées :
3) Actuel : variable booléene qui determinera si le joueur est en train de jouer actuellement ou pas
4) Positions_jetons : dictionnaire qui contiendra la position des jetons du joueur sur chacune des voies
5) Positions_Pions :  dictionnaire qui contiendra la position des pions du joueur sur chacune des voies
6) Nb_pions_restants : variable initialisée en 3 , qui contiendra le nombre de pions non utilisés (restants) du joueur
7) Nb_jetons_restants : variable initialisée en 9 , qui contiendra le nombre de jetons non utilisés (restants) du joueur
8) dés : tuple qio contiendra les dés obtenus , par exemple, si on obtient : 1er dé : 1
                                                                             2e dé : 6     ;  dés sera égale a (1,6,4,3)
                                                                             3e dé : 4
                                                                             4e dé : 3

II) Représentation
exemple :
joueur1 = Joueur ('Rafed', 'Bleu')
Joueur.__repr__(joueur1)

Nom                           : Rafed
Couleur                       : Bleu
Actuel ?                      : Ne joue pas actuellement
Positions des jetons          : {'voie2': -1, 'voie3': -1, 'voie4': -1, 'voie5': -1, 'voie6': -1, 'voie7': -1, 'voie8': -1, 'voie9': -1, 'voie10': -1, 'voie11': -1, 'voie12': -1}
Positions des pions           : {'voie2': -1, 'voie3': -1, 'voie4': -1, 'voie5': -1, 'voie6': -1, 'voie7': -1, 'voie8': -1, 'voie9': -1, 'voie10': -1, 'voie11': -1, 'voie12': -1}
Nombre de pions  restants     : 3
Nombre de jetons restants     : 9
Derniere combinaison des dés  : (0, 0, 0, 0)
"""

class Joueur:
    def __init__(self, nom: str, couleur: str):
        self.nom = nom  # nom des joueurs
        self.couleur = couleur  # couleur du joueur
        self.actuel = False  # bool , si le joueur joue acuellement ou pas
        self.positions_jetons: dict = {"voie2": -1, "voie3": -1, "voie4": -1, "voie5": -1, "voie6": -1, "voie7": -1, "voie8": -1, "voie9": -1, "voie10": -1, "voie11": -1, "voie12": -1}   # les positions des jetons du joueur sur chaque voie
        self.positions_pions: dict= {"voie2": -1, "voie3": -1, "voie4": -1, "voie5": -1, "voie6": -1, "voie7": -1, "voie8": -1, "voie9": -1, "voie10": -1, "voie11": -1, "voie12": -1}  # les positions des pions du joueur
        self.nb_pions_restants = 3  # les pions que possede le joueur
        self.nb_jetons_restants = 9  # les jetons restants
        self.dés = (0, 0, 0, 0)  # les nombres obtenus par les dés
        self.nb_voies_prises = 0

    def __repr__(self):
        if (self.actuel == 1):
            ch_actuel = "Joue actuellement"
        else:
            ch_actuel = "Ne joue pas actuellement"

        print("Joueur : \nNom                           : {} \nCouleur                       : {} \nActuel ?                      : {} \nPositions des jetons          : {} \nPositions des pions           : {} \nNombre de pions  restants     : {} \nNombre de jetons restants     : {}\nDerniere combinaison des dés  : {}".format(self.nom, self.couleur, ch_actuel, self.positions_jetons, self.positions_pions, self.nb_pions_restants, self.nb_jetons_restants, self.dés))
