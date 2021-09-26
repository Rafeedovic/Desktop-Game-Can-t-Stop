"""
Vous trouvez dans le rapport :
                                  I)   Simulation du déroulement du projet
                                  II)  Description des fonctions
                                  III) Répartition du travail
                                  IV)  Remarques sur le projet
"""
from joueur import Joueur
from plateau import Plateau
import random


# ------------------------------------------------------------------------------------------------------------------------------------
def nb_joueurs() -> int:
    while True:
        c = input('Donner le nombre des joueurs (2 ou 3 ou 4)                          : ')
        print()
        if (c == '2') or (c == '3') or (c == '4'):
            break
        else:
            print('Veuillez entrer un nombre valide ! ')
    return int(c)

# ------------------------------------------------------------------------------------------------------------------------------------
def choix_couleur(T: list) -> str:
    while True:
        print("Veuillez choisir une couleur ", T, "   ", end='')

        # complément d'affichage : arrangment des espaces afin d'assurer un affichage bien structuré
        somme = 0
        for i in range(len(T)):
            somme += len(T[i])
        if (len(T) != 4):
            if (len(T) == 3):
                for i in range(4 + (18 - somme)):
                    print(' ', end='')
            elif (len(T) == 2):
                for i in range(4 + (18 - somme) + 4):
                    print(' ', end='')
            else:
                for i in range(4 + (18 - somme) + 8):
                    print(' ', end='')

        print(': ', end='')
        # fin de l'affichage

        ch = input()
        if ch in T:
            break
        else:
            print("Veuillez entrer une couleur valide")

    T.remove(ch)

    return ch

# ------------------------------------------------------------------------------------------------------------------------------------
def creation_joueurs(n: int) -> list:
    Liste_joueurs = []
    Couleurs_possibles = ['Bleu', 'Rouge', 'Noir', 'Jaune']
    for i in range(n):
        # Nom
        nom = input("Donner votre nom ou pseudo                                          : ")
        # Couleur
        couleur = choix_couleur(Couleurs_possibles)
        joueur = Joueur(nom, couleur)
        Liste_joueurs.append(joueur)
        print()
    return Liste_joueurs

# ------------------------------------------------------------------------------------------------------------------------------------
def joueur_actuel(indice_joueur: int, Liste_joueurs: list) -> Joueur:
    return Liste_joueurs[indice_joueur % (len(Liste_joueurs))]

# ------------------------------------------------------------------------------------------------------------------------------------
def combinaisons_dé(joueur: Joueur, plateau: Plateau) -> list:
    liste_comb = []
    comb = (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
    print('Vous avez obtenu comme dés      : ', comb)

    # chargement des donnés
    joueur.dés = comb

    # les sommes possibles a partir des dés, expon a comme dés: 1 ,3 , 7 , 6  // les sommes possibles sont : 1+3=4 & 1+7=8 & 1+6=7 & 3+7=10 & 3+6=9 & 7+6=
    liste_comb.append(str(comb[0] + comb[1]) + ' + ' + str(comb[2] + comb[3]))
    liste_comb.append(str(comb[0] + comb[2]) + ' + ' + str(comb[1] + comb[3]))
    liste_comb.append(str(comb[0] + comb[3]) + ' + ' + str(comb[1] + comb[2]))

    # Suppression des combinaisons doubles
    liste_comb = list(set(liste_comb))

    # affichage des combinaisons porbables
    print('Vos combinaisons probables sont : ', liste_comb, end='')

    # suppression des combinaisons impossibles (exemple avancement sur les colonne 5 et 7 , alors que le joueur n'a qu'un seul pion et ne dispose pas d'un pion sur ces deux colonnes)

    #dans la liste, il ya une combinaison qui indique deux voies déja validés par d'autres joueurs
    nouv_liste_comb = []
    for i in range(len(liste_comb)):
        premiere_voie_choisie: str = "voie" + str(liste_comb[i][:liste_comb[i].index('+') - 1])
        deuxieme_voie_choisie: str = "voie" + str(liste_comb[i][liste_comb[i].index('+') + 2:])
        if ((plateau.voies_prises[premiere_voie_choisie] and plateau.voies_prises[deuxieme_voie_choisie]) == False):
            nouv_liste_comb.append(liste_comb[i])

    liste_comb = nouv_liste_comb

    # determination des colonnes sur lesquelle le joueur a déja un pion
    Liste_colonnes_pions = []
    for i in range(2, 13):
        voie = "voie" + str(i)
        for j in range(len(plateau.map[voie])):
            if ('P' in plateau.map[voie][j]):
                Liste_colonnes_pions.append(str(i))

    Liste_colonnes_pions = list(set(Liste_colonnes_pions))

    nouv_liste_comb = []
    # 1er cas : le joueur a 2 ou 3 pions : pas de restriction des choix
    if (joueur.nb_pions_restants >= 2):
        if (joueur.nb_jetons_restants==1):
            for i in range(len(liste_comb)):
                premiere_voie_choisie: str = "voie" + str(liste_comb[i][:liste_comb[i].index('+') - 1])
                deuxieme_voie_choisie: str = "voie" + str(liste_comb[i][liste_comb[i].index('+') + 2:])
                if (((joueur.positions_jetons[premiere_voie_choisie]!=-1) and (joueur.positions_jetons[deuxieme_voie_choisie]==-1)) or ((joueur.positions_jetons[premiere_voie_choisie]==-1) and (joueur.positions_jetons[deuxieme_voie_choisie]!=-1)) or ((joueur.positions_jetons[premiere_voie_choisie]!=-1) and (joueur.positions_jetons[deuxieme_voie_choisie]!=-1))):
                    nouv_liste_comb.append(liste_comb[i])
            return nouv_liste_comb

        elif (joueur.nb_jetons_restants==0):
            for i in range(len(liste_comb)):
                premiere_voie_choisie: str = "voie" + str(liste_comb[i][:liste_comb[i].index('+') - 1])
                deuxieme_voie_choisie: str = "voie" + str(liste_comb[i][liste_comb[i].index('+') + 2:])
                if (joueur.positions_jetons[premiere_voie_choisie]!=-1) and (joueur.positions_jetons[deuxieme_voie_choisie]!=-1):
                    nouv_liste_comb.append(liste_comb[i])
            return nouv_liste_comb

        return liste_comb

    # 2eme cas : le joueur a 1 seul pion ou 1 seul jeton
    nouv_liste_comb = []
    if (joueur.nb_pions_restants == 1) or (joueur.nb_jetons_restants == 1):                     # le joueur n'a qu' un seul pion : soit il place ce pion + avance un autre pion / soit il place ce pion seulement
        # 1er sous cas : le joueur a déja un pion posé sur l'une des colonnes issues du tirage
        for i in range(len(liste_comb)):
            for k in range(len(Liste_colonnes_pions)):
                if (Liste_colonnes_pions[k] in liste_comb[i]):
                    nouv_liste_comb.append(liste_comb[i])
        nouv_liste_comb = list(set(nouv_liste_comb))
        return nouv_liste_comb

    # 3eme cas :  le joueur a 0 pion ou 0 jetons : le joueur ne qu'a avancer un de ces pions qui existent sur la map
    elif (joueur.nb_pions_restants == 0) or (joueur.nb_jetons_restants == 0):
        # suppression des colonnes simples
        if (len(Liste_colonnes_pions) != 0):
            for i in range(len(liste_comb)):
                if (len(liste_comb) != 0) and ((liste_comb[i][0] in Liste_colonnes_pions) or (liste_comb[i][4] in Liste_colonnes_pions)):
                    nouv_liste_comb.append(liste_comb[i])
        nouv_liste_comb = list(set(nouv_liste_comb))
        return nouv_liste_comb

    return liste_comb

# ------------------------------------------------------------------------------------------------------------------------------------
def choix_comb(liste_comb: list) -> str:
    print("Vos combinaisons possibles sont :  ", end='')

    # Affichage des combinaisons
    print(liste_comb)

    #demande de saisie
    print("Veuillez saisir l'indice de la combinaison voulue : ", end='')
    while True:
        ch = input()
        if (ch == '0') or (ch == '1') or (ch == '2'):
            if ((int(ch) >= 0) and (int(ch) < len(liste_comb))):
                break
        else:
            print('Veuillez entrer un indice valide                  : ', end='')


    return liste_comb[int(ch)]

# ------------------------------------------------------------------------------------------------------------------------------------
def exécution_combinaisons(plateau: Plateau, joueur: Joueur, comb_choisie: str):
    premiere_voie_choisie: str = "voie"+str(comb_choisie[:comb_choisie.index('+') - 1])
    deuxieme_voie_choisie: str = "voie"+str(comb_choisie[comb_choisie.index('+') + 2:])

#fixation du nombre d"exécutions (soit un seul deplacment , soit 2 deplacements)
    #aucune contrainte
    nombre_executions: int = 2

    #nombre_executions = 1
    # contrainte 1 : le joueur a 0 pions mais dans la combinaison choisie, un seul deplacement est possible
    if (joueur.nb_pions_restants==0) and (((joueur.positions_pions[premiere_voie_choisie]!=-1) and (joueur.positions_pions[deuxieme_voie_choisie]==-1)) or ((joueur.positions_pions[premiere_voie_choisie]==-1) and (joueur.positions_pions[deuxieme_voie_choisie]!=-1))):
        nombre_executions = 1

    # contrainte 2 : une voie parmi les deux voies choisie est validée
    if ((plateau.voies_prises[premiere_voie_choisie]) and (plateau.voies_prises[deuxieme_voie_choisie]) ==False):
        nombre_executions = 1

    #nombre_executions = 0
    #les deux voies choisies sont validés
    if ((plateau.voies_prises[premiere_voie_choisie]) and (plateau.voies_prises[deuxieme_voie_choisie]) == True):
        nombre_executions = 0

#execution des deplacement(s)

    for i in range(nombre_executions):
        voie=""
        if (nombre_executions==2):
            indice_voie_choisie = comb_choisie[:comb_choisie.index('+') - 1]    # on copie en sous chaine l'indice la premiere voie, exp : "3 + 5" pour avoir 3, on copie de la position 0 jusqu'a la position 1
            if (i == 1):                                                        # exécution du 2eme deplacement si la combinaison est double exp : "5+7" cad voie5 et voie7
                indice_voie_choisie = comb_choisie[comb_choisie.index('+') + 2:]  # on copie en sous chaine l'indice la deuxieme voie, exp : "3 + 5" pour avoir 5, on copie de la position de ' +' +2, jusqu'a la fin de la chaine

            voie: str = "voie" + indice_voie_choisie

        elif (nombre_executions==1):
            #contrainte 1
            if (joueur.positions_pions[premiere_voie_choisie]!=-1):
                voie= premiere_voie_choisie
            else:
                voie= deuxieme_voie_choisie

            #contrainte 2
            if (plateau.voies_prises[premiere_voie_choisie]==False) and (plateau.voies_prises[deuxieme_voie_choisie]==True):
                voie= premiere_voie_choisie
            elif (plateau.voies_prises[deuxieme_voie_choisie]==False) and (plateau.voies_prises[premiere_voie_choisie]==True):
                voie= deuxieme_voie_choisie

        # position du pion dans la voie
        pos_ancien_pion = -1
        for j in range(len(plateau.map[voie])):
            if ('P' in plateau.map[voie][j]):
                pos_ancien_pion = j

        pos_ancien_jeton = -1
        for k in range(len(plateau.map[voie])):
            if (joueur.couleur[0] in plateau.map[voie][k]):
                pos_ancien_jeton = k
        if (not('P' in plateau.map[voie][len(plateau.map[voie])-1])) and (not(joueur.couleur[0] in plateau.map[voie][len(plateau.map[voie])-1])):  #le pion ou le jeton n'est pas au sommet
            if (joueur.positions_pions[voie] == -1) and (joueur.positions_jetons[voie] == -1):  # dans cette voie, ni pion ni jeton
                if (plateau.map[voie][0] == '.'):
                    plateau.map[voie][0] = 'P'

                else:
                    plateau.map[voie][0] += '+P'

            elif (pos_ancien_jeton >= 0) and (joueur.positions_pions[voie] == -1):  # dans cette voie il n y a que un jeton (pas de pions)
                if (plateau.map[voie][pos_ancien_jeton + 1] == '.'):
                    plateau.map[voie][pos_ancien_jeton + 1] = 'P'
                else:
                    plateau.map[voie][pos_ancien_jeton + 1] += '+P'


            elif ((plateau.map[voie][pos_ancien_pion + 1] != '.') and (plateau.map[voie][pos_ancien_pion + 1] != joueur.couleur[0])):  # dans cette voie il ya un jeton d'un autre joueur +  pas de pions du joueur actuel
                plateau.map[voie][pos_ancien_pion + 1] += '+P'
                if ('P' in plateau.map[voie][pos_ancien_pion]):
                    plateau.map[voie][pos_ancien_pion] = plateau.map[voie][pos_ancien_pion].replace('P', '.')
                elif ('+P' in plateau.map[voie][pos_ancien_pion]):
                    plateau.map[voie][pos_ancien_pion] = plateau.map[voie][pos_ancien_pion].replace('+P', '.')

                if (pos_ancien_jeton != -1):
                    plateau.map[voie][pos_ancien_jeton] = '.'

            else:  # dans cette voie, il ya un jeton du joueur actuel + un pion de ce joueur
                if (plateau.map[voie][pos_ancien_pion + 1] == '.'):
                    plateau.map[voie][pos_ancien_pion + 1] = 'P'
                else:
                    plateau.map[voie][pos_ancien_pion + 1] += '+P'
                # enlevement du pion de l'ancien position
                if (plateau.map[voie][pos_ancien_pion] == 'P'):
                    plateau.map[voie][pos_ancien_pion] = plateau.map[voie][pos_ancien_pion].replace('P', '.')
                else:
                    plateau.map[voie][pos_ancien_pion] = plateau.map[voie][pos_ancien_pion].replace('+P', '')

            joueur.positions_pions[voie] += 1
            joueur.nb_pions_restants -= 1

            somme = 0
            for j in range(2, 13):
                voie = "voie" + str(j)
                if (joueur.positions_pions[voie] != -1):
                    somme += 1
            joueur.nb_pions_restants = 3 - somme

            if (joueur.nb_pions_restants < 0):  # le joueur n'a plus de pions restants
                joueur.nb_pions_restants = 0

            print()
            """
            if (comb_choisie[:comb_choisie.index('+') - 1]==comb_choisie[comb_choisie.index('+') + 2:]) and (joueur.nb_pions_restants!=0) and (nombre_executions==2):             #un double deplacement sur la meme colonne
                joueur.nb_pions_restants += 1
            """

    plateau.__repr__()

# ------------------------------------------------------------------------------------------------------------------------------------
def enlevement_pions(plateau: Plateau):
    for i in range(2, 13):
        voie = "voie" + str(i)
        for j in range(len(plateau.map[voie])):
            if ('+P' in plateau.map[voie][j]):
                plateau.map[voie][j] = plateau.map[voie][j].replace('+P', '')
            elif ('P' in plateau.map[voie][j]):
                plateau.map[voie][j]='.'

# ------------------------------------------------------------------------------------------------------------------------------------
def remplacement_pions_par_jetons(joueur: Joueur, plateau: Plateau):
    for i in range(2, 13):
        voie = "voie" + str(i)
        for j in range(len(plateau.map[voie])):
            if ('P' in plateau.map[voie][j]):
                plateau.map[voie][j]= plateau.map[voie][j].replace('P', joueur.couleur[0])      # on marque la derniere position des pions , on y pose les jetons
                joueur.positions_jetons[voie] = j                                              # on note la derniere position de ces jetons dans le dictionnaire positions_jetons du joueur

# ------------------------------------------------------------------------------------------------------------------------------------
def validation_voies(plateau: Plateau, joueur: Joueur, Liste_joueurs: list):
    for i in range(2, 13):
        voie="voie"+str(i)
        if (joueur.couleur[0] in plateau.map[voie][len(plateau.map[voie])-1]) or (('+'+joueur.couleur[0]) in plateau.map[voie][len(plateau.map[voie])-1]) or ((joueur.couleur[0]+'+') in plateau.map[voie][len(plateau.map[voie])-1]):
            #le joueur a validé cette voie  ---> enlevement des jetons des autres joueur
            for j in range(len(plateau.map[voie])-1):
                if (plateau.map[voie][j]!='.'):
                    for indice_joueur in range(len(Liste_joueurs)):
                        if (Liste_joueurs[indice_joueur].couleur[0] in plateau.map[voie][j]):
                            Liste_joueurs[indice_joueur].nb_jetons_restants +=1
                plateau.map[voie][j]=joueur.couleur[0]

            plateau.voies_prises[voie]=True

# ------------------------------------------------------------------------------------------------------------------------------------
def vérification_validation_trois_voies(plateau: Plateau, joueur: Joueur)->bool:
    somme_voies_validés = 0 
    for i in range(2, 13):
        voie="voie"+str(i)
        if (joueur.couleur[0] in plateau.map[voie][len(plateau.map[voie])-1]) or (('+'+joueur.couleur[0]) in plateau.map[voie][len(plateau.map[voie])-1]) or ((joueur.couleur[0]+'+') in plateau.map[voie][len(plateau.map[voie])-1]):
            somme_voies_validés += 1
    joueur.nb_voies_prises = somme_voies_validés
    if (somme_voies_validés>=3):
        return True
    return False

# ------------------------------------------------------------------------------------------------------------------------------------
def deux_jetons_du_meme_joueur_sur_meme_colonne(plateau: Plateau, joueur: Joueur):
    occ = 0
    for i in range(2, 13):
        voie = "voie" + str(i)
        for j in range(len(plateau.map[voie])):
            occ = occ + plateau.map[voie][j].count(joueur.couleur[0])
        if (occ>1):
            pos=-1
            for k in range(len(plateau.map[voie]) - 1, 0, -1):
                if (joueur.couleur[0] in plateau.map[voie][k]):
                    pos = k
                    break


            for l in range(pos):
                if (('+'+joueur.couleur[0]) in plateau.map[voie][l]):
                    plateau.map[voie][l] = plateau.map[voie][l].replace(('+'+joueur.couleur[0]), '')
                if ((joueur.couleur[0]+'+') in plateau.map[voie][l]):
                    plateau.map[voie][l] = plateau.map[voie][l].replace((joueur.couleur[0]+'+'), '')

                if (joueur.couleur[0] in plateau.map[voie][l]):
                    plateau.map[voie][l] = plateau.map[voie][l].replace(joueur.couleur[0], '.')
        occ = 0

# ------------------------------------------------------------------------------------------------------------------------------------
def calcul_nombre_jetons_restants(plateau: Plateau, joueur: Joueur)->int:
    n=0
    for i in range(2, 13):
        voie = "voie"+str(i)
        #si la voie est validé par le joueur, on compte un seul jeton dans cette voie, qui est le jeton au sommet
        if (plateau.voies_prises[voie]) and ((joueur.couleur[0]) in (plateau.map[voie][len(plateau.map[voie])-1])):
            n = n + 1
        #sinon on parcours tous le plateau
        else:
            for j in range(len(plateau.map[voie])):
                if (joueur.couleur[0]) in plateau.map[voie][j]:
                    n = n + 1

    jeton_restant = 9 -n
    if (jeton_restant>=0):
        return jeton_restant
    return 0

# ------------------------------------------------------------------------------------------------------------------------------------
def la_voie_choisie_est_validé_par_un_autre_joueur(plateau: Plateau):
    for i in range(2, 13):
        voie = "voie"+str(i)
        if (plateau.map[voie][len(plateau.map[voie])-1])!='.':
            for j in range(len(plateau.map[voie])):
                plateau.map[voie][j] = plateau.map[voie][len(plateau.map[voie])-1]

# ------------------------------------------------------------------------------------------------------------------------------------

def main():
    # initialistion + création joueurs
    nombre_joueurs = nb_joueurs()
    Liste_joueurs = creation_joueurs(nombre_joueurs)

    # initialisation
    plateau = Plateau()
    joueur = Joueur('', '')

    # initialisation des tours
    indice_joueur = 0

    while (plateau.nb_voies_prises<3):
        # Appel du joueur actuel
        joueur: Joueur = joueur_actuel(indice_joueur, Liste_joueurs)

        joueur.actuel = True
        plateau.__repr__()

        while True:
            print()
            print("Le joueur actuel est            : ", joueur.nom)
            print("Votre couleur est               : ", joueur.couleur)
            print()

            joueur.nb_jetons_restants = calcul_nombre_jetons_restants(plateau, joueur)
            print("Vous avez                       : ", joueur.nb_jetons_restants, " jetons restants")
            print("Vous avez à disposition         : ", joueur.nb_pions_restants, " pion(s) libre(s)")

            # Lancement des dés
            liste_comb = combinaisons_dé(joueur, plateau)

            # Cas de perte : les combinaisons ne sont pas éxécutables
            if (len(liste_comb) == 0):
                print()
                print('Perte ! ')
                # enlevement des pions de la map
                enlevement_pions(plateau)
                break

            # pas de perte : les combinaisons sont éxécutables
            # combinaison choisie
            print()
            comb_choisie = choix_comb(liste_comb)
            la_voie_choisie_est_validé_par_un_autre_joueur(plateau)
            exécution_combinaisons(plateau, joueur, comb_choisie)
            la_voie_choisie_est_validé_par_un_autre_joueur(plateau)

            # Continuer ou stopper
            print('Il vous reste', joueur.nb_pions_restants, ' pion(s),', end=' ')
            while True:
                réponse = input('voulez-vous continuer ? (oui ou non) ')
                if (réponse == 'oui') or (réponse == 'non'):
                    break

            # stopper:
            # remplacement des pions pas les jetons de la mm couleur que le joueur + chargements des nouvelles données
            if (réponse == 'non'):
                remplacement_pions_par_jetons(joueur, plateau)

                # chargement des données
                deux_jetons_du_meme_joueur_sur_meme_colonne(plateau, joueur)
                joueur.actuel = False
                joueur.positions_pions = {"voie2": -1, "voie3": -1, "voie4": -1, "voie5": -1, "voie6": -1, "voie7": -1, "voie8": -1, "voie9": -1, "voie10": -1, "voie11": -1, "voie12": -1}
                joueur.nb_pions_restants = 3
                break
                        
            # continuer: refaire la mm chose
            plateau.__repr__()
            
        # chargement des données
        joueur.actuel = False
        joueur.positions_pions = {"voie2": -1, "voie3": -1, "voie4": -1, "voie5": -1, "voie6": -1, "voie7": -1, "voie8": -1, "voie9": -1, "voie10": -1, "voie11": -1, "voie12": -1}
        joueur.nb_pions_restants = 3

        indice_joueur += 1

        #vérifions si le joueur a validé une voie ou non
        validation_voies(plateau, joueur, Liste_joueurs)

        #vérification de la condition de gain
        if (vérification_validation_trois_voies(plateau, joueur)):
            break
    
    plateau.__repr__()
    print("Le joueur gagnant est : ", joueur.nom, " Féliciations ! ")



main()
