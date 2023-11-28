def check_coin(coin: int) -> bool:
    """
    Controleert of een munt wordt toegelaten.
    """
    if coin == 25 or coin == 10 or coin == 5:
        return True
    else:
        return False

    

def determine_due(due: int, coin: int) -> int:
    """
    Bepaalt hoeveel nog moet worden betaald nadat een munt is
    ingeworpen. Uitkomst verandert alleen als coin één van de
    toegestane munten is.
    """
    # for loop
    # eerst check_coin
    
    toegestaan = [25,10,5]
    if coin in toegestaan:
        return due-coin
    else:
        return due

#if __name__ == '__main__':
