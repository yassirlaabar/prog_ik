def is_acidic(ph: float) -> bool:
    """
    De functie laat zien of de input acidic is

    >>> is_acidic(3)
    True
    >>> is_acidic(9)
    False
    >>> is_acidic(7)
    False
    """
    if ph < 7.0:
        return True
    else:
        return False

if __name__ == '__main__':
    ph = float(input("Enter the pH level: "))
    if is_acidic(ph):
        print("It's acidic!")
    else:
        print("It's alkaline!")
