"""
Classe Plateau, le plateau aura 3 attributs
I) Construction
**Données:

**Genérées:
1) Map : dictionnaire qui contiendra , les pions et les jetons du joueur (le plateau lui-meme)
2) Voies_prises : dictionnaire qui contiendra les information de validation des colonnes : False : la colonne n'est pas validées // True : la colonne est validée par un joueur
3) Nb_voies_prise : variable qui contiendra le nombre des voies validés, si nb_voies_prises = 3, le jeu prend fin !

II)Representation
-- L'affichage du plateau est en verticale
-- L'affichage vertical était complexe:
   En fait, pour assuerer que les cases seront toujours centrées, le nombre d'espaces entre deux cases consécutives est automatisé:
   ** La longueur minimale d'une case est egale à 1  exp : 'R'           c-a-d jeton rouge
   ** La longueur maximale d'une case est égale à 7   exp : 'R+B+N+J'     c-a-d jeton rouge avec jeton bleu avec jeton noir avec jeton jaune
   ** Les valeurs possibles de la longuer d'une case sont : 1 (un jeton) ou 3 (deux jetons) ou 5 (trois jetons) ou 7 (quatre jetons)
   ** Pour généraliser ces 4 cas possible, on considere la case comme une chaine centrée respectivement en 1 ou 2 ou 3 ou 4
      exp : pour quatre jetons, la longuer = 7 : 'R+B+N+J' est equivalent à aaaaaa , dont le centre | est '+' , 'R+B|N+J'
            pour trois jetons, la longuer = 5 : 'R+B+N' est equivalent à aa|aa , dont le centre | est 'B' , 'R+|+N'
            pour deux jetons, la longuer = 3 : 'R+B' est equivalent à a|a , dont le centre | est '+' , 'R|B'
            pour un jeton, la longuer = 1 : 'R' est equivalent à | , dont le centre | est 'R' , 'R'
   ** Pour organiser l'affichage, on affiche les espaces entre deux cases consécutifs d'une maniere automatique
      nb_espace = 7 - (longueur_case_precedante // 2 ) - (longueur_case_suivante //2)
      expl1:
                              .
                              .
                      .       .
                      .       .
              .    aaa|aaa bbb|bbb
              .       .       .
              .       .       .
      le nombre d'espaces entre ces deux cases = 7 - (len('aaa|aaa')//2) - (len('bbb|bbb')//2) = 7 - 3 - 3 = 1
      donc on affichera la case a gauche , puis 1 espace, puis la case a droite

      expl2:
                              .
                              .
                      .       .
                      .       .
              .     R+N+J     B
              .       .       .
              .       .       .

      le nombre d'espaces entre ces deux cases = 7 - (len('R+N+J')//2) - (len('B')//2) = 7 - 2 - 0 = 5
      donc on affichera la case a gauche 'R+N+J' , puis 5 espace, puis la case a droite 'B'

      expl3:
                            .
                            .
                    .       .
                    .       .
            .       N       J
            .       .       .
            .       .       .

      le nombre d'espaces entre ces deux cases = 7 - (len('N')//2) - (len('J')//2) = 7 - 0 - 0 = 7
      donc on affichera la case a gauche 'N' , puis 7 espace, puis la case a droite 'J'

      Remarque : si la case est vide, case est égale à '.', sa longeur sera egale à 1, cette methode est donc appliquable a toutes les cases du plateau, vides étaient ou remplies


** Exemple d'éxécution :
plateau1=Plateau()
Plateau.__repr__(plateau1)

plateau1.map["voie7"][12]='R+P'
plateau1.map["voie9"][5]='R+B+P'
plateau1.map["voie9"][8]='R'
plateau1.map["voie9"][0]='N+B+J'
plateau1.map["voie9"][2]='R+N'
plateau1.map["voie10"][2]='R+N'
plateau1.map["voie10"][0]='R'

Plateau.__repr__(plateau1)


"""
class Plateau:
    def __init__(self):
        self.map: dict ={"voie2": ['.', '.', '.'],
                         "voie3": ['.', '.', '.', '.', '.'],
                         "voie4": ['.', '.', '.', '.', '.', '.', '.'],
                         "voie5": ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         "voie6": ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         "voie7": ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         "voie8": ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         "voie9": ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         "voie10": ['.', '.', '.', '.', '.', '.', '.'],
                         "voie11": ['.', '.', '.', '.', '.'],
                         "voie12": ['.', '.', '.']}
        self.voies_prises ={"voie2": False, "voie3": False, "voie4": False, "voie5": False, "voie6": False, "voie7": False, "voie8": False, "voie9": False, "voie10": False, "voie11": False, "voie12": False}
        self.nb_voies_prises = 0

    def __repr__(self):
        print('*******************************************************************************************')
        print()

        #intialisation
        nb_cases = 0
        premiere_case = 0
        derniere_case = 0
        ligne = 0
        def voiee(n: int):
            return "voie" + str(n)

        for ligne in range(12, 1, -2):
            # détermination des nombres de cases a afficher dans cette ligne || esp: pour i=12, nb_cases=1 // i=10 , nb_cases=3 // i=2, nb_cases=11
            nb_cases = 13 - ligne

            # détermination de l'indice de la premiere cases a afficher dans cette ligne
            if (ligne == 12):
                premiere_case = 7
            elif (ligne == 10):
                premiere_case = 6
            elif (ligne == 8):
                premiere_case = 5
            elif (ligne == 6):
                premiere_case = 4
            elif (ligne == 4):
                premiere_case = 3
            elif (ligne == 2):
                premiere_case = 2
            else:
                premiere_case = 0

            # determination de la derniere case a afficher
            derniere_case = 7 + (7 - premiere_case)

            # Affichage de la nieme ligne COMPLETE -------------------------------------------------------------------------------
            # affichages des espaces a gauche de la map
            for compteur in range((47 - 4 * (nb_cases)) - len(self.map[voiee(premiere_case)][ligne]) // 2):
                print(' ', end='')

            # affichage de la premiere case
            if (ligne == 12):
                print(self.map[voiee(premiere_case)][ligne])
            else:
                print(self.map[voiee(premiere_case)][ligne], end='')

            # affichage du reste des cases
            for compteur in range(premiere_case + 1, derniere_case + 1):
                nb_espaces_restantes_de_la_case_precedante = 3 - (len(self.map[voiee(compteur - 1)][ligne]) // 2)
                nb_espaces_restantes_de_la_case_suivante = 4 - (len(self.map[voiee(compteur)][ligne]) // 2)
                for i in range(nb_espaces_restantes_de_la_case_precedante + nb_espaces_restantes_de_la_case_suivante):
                    print(' ', end='')

                # si c'est la derniere case, on retourne a la ligne apres son affichage, sinon on l'affiche avec end=''
                if (compteur == derniere_case):
                    print(self.map[voiee(derniere_case)][ligne])
                else:
                    print(self.map[voiee(compteur)][ligne], end='')

            # ------------------------------------------------------------------------------------------------------------------------------
            # Affichage de la ligne juste en dessous (il s'agit juste de remplacer ligne par ligne-1

            # affichages des espaces a gauche de la map
            for compteur in range((47 - 4 * (nb_cases)) - len(self.map[voiee(premiere_case)][ligne - 1]) // 2):
                print(' ', end='')

            # affichage de la premiere case
            if (ligne == 12):
                print(self.map[voiee(premiere_case)][ligne - 1])
            else:
                print(self.map[voiee(premiere_case)][ligne - 1], end='')

            # affichage du reste des cases
            for compteur in range(premiere_case + 1, derniere_case + 1):
                nb_espaces_restantes_de_la_case_precedante = 3 - (len(self.map[voiee(compteur - 1)][ligne - 1]) // 2)
                nb_espaces_restantes_de_la_case_suivante = 4 - (len(self.map[voiee(compteur)][ligne - 1]) // 2)
                for i in range(nb_espaces_restantes_de_la_case_precedante + nb_espaces_restantes_de_la_case_suivante):
                    print(' ', end='')

                # si c'est la derniere case, on retourne a la ligne apres son affichage, sinon on l'affiche avec end=''
                if (compteur == derniere_case):
                    print(self.map[voiee(derniere_case)][ligne - 1])
                else:
                    print(self.map[voiee(compteur)][ligne - 1], end='')

        # ------------------------------------------------------------------------------------------------------------------------------
        # Affichage de la derniere ligne isolamment

        # affichages des espaces a gauche de la map
        for compteur in range((47 - 4 * (nb_cases)) - len(self.map[voiee(premiere_case)][ligne - 2]) // 2):
            print(' ', end='')

        # affichage de la premiere case
        print(self.map[voiee(premiere_case)][ligne - 2], end='')

        # affichage du reste des cases
        for compteur in range(premiere_case + 1, derniere_case + 1):
            nb_espaces_restantes_de_la_case_precedante = 3 - (len(self.map[voiee(compteur - 1)][ligne - 2]) // 2)
            nb_espaces_restantes_de_la_case_suivante = 4 - (len(self.map[voiee(compteur)][ligne - 2]) // 2)
            for i in range(nb_espaces_restantes_de_la_case_precedante + nb_espaces_restantes_de_la_case_suivante):
                print(' ', end='')

            # si c'est la derniere case, on retourne a la ligne apres son affichage, sinon on l'affiche avec end=''
            if (compteur == derniere_case):
                print(self.map[voiee(derniere_case)][ligne - 2])
            else:
                print(self.map[voiee(compteur)][ligne - 2], end='')

        # ------------------------------------------------------------------------------------------------------------------------------
        # Affichage les numéros des colonnes
        print()
        print('   {}       {}       {}       {}       {}       {}       {}       {}      {}      {}      {}   '.format(
            '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))

        print()
        print('*******************************************************************************************')
