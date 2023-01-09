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
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")
    elif type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen")
    cellule = {const.CONTENU:contenu, const.VISIBLE:visible}
    return cellule