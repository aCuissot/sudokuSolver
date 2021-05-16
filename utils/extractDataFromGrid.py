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
