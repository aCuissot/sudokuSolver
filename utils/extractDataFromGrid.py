import constantes


def missingNumbersInEntity(entity):
    """

    :param entity: the entity (raw, column, square)
    :return: a list of the missing numbers in this entity
    """
    missing = []
    for i in range(1, constantes.SIZEOFALINE+1):
        if not str(i) in entity:
            missing.append(str(i))
    return missing


def getSquareConnectedRawsAndColumns(squareNumber):
    """

    :param squareNumber: the number of the square
    :return: 2 lists: one for the raws connected to the square and one for the columns
    """
    raws = list(range(constantes.SIZEOFASQUARE * (squareNumber//constantes.SIZEOFASQUARE), constantes.SIZEOFASQUARE * (squareNumber//constantes.SIZEOFASQUARE + 1)))
    columns = list(range(constantes.SIZEOFASQUARE * (squareNumber%constantes.SIZEOFASQUARE), constantes.SIZEOFASQUARE * (squareNumber%constantes.SIZEOFASQUARE + 1)))
    return raws, columns
