# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(li:int,co:int) -> list:
    if type(li) != int or type(co) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes ({type(li)}) ou de colonnes ({type(co)}) n’est pas un entier. »")
    elif li <= 0 or co <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes ({li}) ou de colonnes ({co}) est négatif ou nul.")
    tab = []
    for i in range(0,li):
        ligne = []
        for j in range(0,co):
            cellule = construireCellule(0, False)
            ligne += [cellule]
        tab.append(ligne)
    return tab

def getNbLignesGrilleDemineur(grille:list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille)

def getNbColonnesGrilleDemineur(grille:list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille.")
    return len(grille[0])

def isCoordonneeCorrecte(grille:list,coord:tuple) -> bool:
    if type(grille) != list or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    correct = True
    if getLigneCoordonnee(coord) < 0 or getLigneCoordonnee(coord) >= getNbLignesGrilleDemineur(grille):
        correct = False
    elif getColonneCoordonnee(coord) < 0 or getColonneCoordonnee(coord) >= getNbColonnesGrilleDemineur(grille):
        correct = False
    return correct

def getCelluleGrilleDemineur(grille:list,coord:tuple) -> dict:
    if type(grille) != list or type(coord) != tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    elif not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille:list,coord:tuple) -> int:
    cellule = getCelluleGrilleDemineur(grille,coord)
    return getContenuCellule(cellule)

def setContenuGrilleDemineur(grille:list,coord:tuple,contenu:int) -> None:
    cellule = getCelluleGrilleDemineur(grille,coord)
    setContenuCellule(cellule,contenu)
    return None

def isVisibleGrilleDemineur(grille:list,coord:tuple) -> bool:
    cellule = getCelluleGrilleDemineur(grille,coord)
    return isVisibleCellule(cellule)

def setVisibleGrilleDemineur(grille:list,coord:tuple,visible:bool) -> None:
    cellule = getCelluleGrilleDemineur(grille, coord)
    setVisibleCellule(cellule,visible)
    return None

def contientMineGrilleDemineur(grille:list,coord:tuple) -> bool:
    cellule = getCelluleGrilleDemineur(grille,coord)
    mine = False
    if getContenuCellule(cellule) == const.ID_MINE:
        mine = True
    return mine

def getCoordonneeVoisinsGrilleDemineur(grille:list,coord:tuple) -> list:
    if type(grille) != list or type(coord) != tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    lst_coordVoisines = []
    for i in range(coord[0]-1,coord[0]+2):
        for j in range(coord[1]-1,coord[1]+2):
            if isCoordonneeCorrecte(grille,(i,j)) and (i,j) != coord:
                lst_coordVoisines.append((i,j))
    return lst_coordVoisines

def placerMinesGrilleDemineur(grille:list,nb:int,coord:tuple) -> None:
    if nb < 0 or nb > len(grille)*len(grille[0])-1:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    nb_minesPlaces = 0
    lst_coordMines = []
    while nb_minesPlaces < nb:
        coordMine = (randint(0,len(grille)-1),randint(0,len(grille[0])-1))
        if coordMine not in lst_coordMines and coordMine != coord:
            lst_coordMines.append(coordMine)
            setContenuGrilleDemineur(grille,coordMine,const.ID_MINE)
            nb_minesPlaces += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille:list) -> None:
    for i in range(0,len(grille)):
        for j in range(0,len(grille[i])):
            if getContenuGrilleDemineur(grille,(i,j)) != const.ID_MINE:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille,(i,j))
                compteur = 0
                for k in range(len(voisins)):
                    if getContenuGrilleDemineur(grille,voisins[k]) == const.ID_MINE:
                        compteur += 1
                setContenuGrilleDemineur(grille,(i,j),compteur)
    return None

def getNbMinesGrilleDemineur(grille:list) -> int:
    if type(grille) != list:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    compteur = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if getContenuGrilleDemineur(grille, (i, j)) == const.ID_MINE:
                compteur += 1
    return compteur

def getAnnotationGrilleDemineur(grille:list,coord:tuple) -> str:
    cellule = getCelluleGrilleDemineur(grille, coord)
    return getAnnotationCellule(cellule)

def getMinesRestantesGrilleDemineur(grille:list) -> int:
    nb = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            annotation = getAnnotationGrilleDemineur(grille,(i,j))
            if annotation == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb

def gagneGrilleDemineur(grille:list) -> bool:
    fini = True
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i, j))
            if (getContenuCellule(cellule) != const.ID_MINE and isVisibleCellule(cellule) == False) or (getContenuCellule(cellule) == const.ID_MINE and isVisibleCellule(cellule) == True) or (getContenuCellule(cellule) == const.ID_MINE and getAnnotationCellule(cellule) != const.FLAG):
                fini = False
    return fini

def perduGrilleDemineur(grille:list) -> bool:
    perdu = False
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille, (i, j))
            if getContenuCellule(cellule) == const.ID_MINE and isVisibleCellule(cellule) == True:
                perdu = True
    return perdu

def reinitialiserGrilleDemineur(grille:list) -> None:
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            cellule = getCelluleGrilleDemineur(grille,(i,j))
            reinitialiserCellule(cellule)
    return None

def decouvrirGrilleDemineur(grille:list,coord:tuple) -> set:
    lst_CellulesDecouvertes = []
    lst_CellulesParcourues = []
    lst_CellulesDecouvertes.append(coord)
    lst_CellulesParcourues.append(coord)
    i = 0
    while i < len(lst_CellulesParcourues):
        if getContenuGrilleDemineur(grille,lst_CellulesParcourues[i]) == 0:
            lst_voisins = getCoordonneeVoisinsGrilleDemineur(grille,lst_CellulesParcourues[i])
            for j in lst_voisins:
                if not (j in lst_CellulesDecouvertes):
                    lst_CellulesDecouvertes.append(j)
                if not (j in lst_CellulesParcourues):
                    lst_CellulesParcourues.append(j)
        i += 1
    return set(lst_CellulesDecouvertes)