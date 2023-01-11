# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(nb:int) -> bool:
    correct = True
    if type(nb) != int:
        correct = False
    elif nb < const.ID_MINE or nb > 8:
        correct = False
    return correct

def construireCellule(contenu:int=0,visible:bool=False) -> dict:
    if contenu < const.ID_MINE or contenu > 8:
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct.")
    elif type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen.")
    cellule = {const.CONTENU:contenu, const.VISIBLE:visible, const.ANNOTATION:None}
    return cellule

def getContenuCellule(dico:dict) -> int:
    cellule_correct = type_cellule(dico)
    if cellule_correct == False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return dico[const.CONTENU]

def isVisibleCellule(dico:dict) -> bool:
    cellule_correct = type_cellule(dico)
    if cellule_correct == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return dico[const.VISIBLE]

def setContenuCellule(dico:dict,contenu:int) -> None:
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if contenu < const.ID_MINE or contenu > 8:
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    elif not type_cellule(dico)==True:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    dico[const.CONTENU] = contenu
    return None

def setVisibleCellule(dico:dict,visible:bool) -> None:
    if not type_cellule(dico)==True:
        raise TypeError("setVisible Cellule : Le premier paramètre n’est pas une cellule.")
    elif type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen.")
    dico[const.VISIBLE] = visible
    return None

def contientMineCellule(dico:dict) -> bool:
    if not type_cellule(dico)==True:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    contient = False
    if dico[const.CONTENU] == const.ID_MINE:
        contient = True
    return contient

def isAnnotationCorrecte(annotation:str) -> bool:
    lst_annotations = [None,const.FLAG,const.DOUTE]
    correcte = True
    if annotation not in lst_annotations:
        correcte = False
    return correcte

def getAnnotationCellule(cellule:dict) -> str:
    if type(cellule) != dict:
        raise TypeError(f"getAnnotationCellule : le paramètre cellule ({type(cellule)}) n’est pas une cellule")
    if len(cellule) < 3:
        annotation = None
    else:
        annotation = cellule[const.ANNOTATION]
    return annotation

def changeAnnotationCellule(cellule:dict) -> None:
    if type(cellule) != dict:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule.")
    annotation = getAnnotationCellule(cellule)
    if annotation == None:
        cellule[const.ANNOTATION] = const.FLAG
    elif annotation == const.FLAG:
        cellule[const.ANNOTATION] = const.DOUTE
    else:
        cellule[const.ANNOTATION] = None
    return None

def reinitialiserCellule(cellule:dict) -> None:
    setContenuCellule(cellule,0)
    setVisibleCellule(cellule,False)
    cellule[const.ANNOTATION] = None
    return None