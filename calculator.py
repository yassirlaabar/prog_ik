def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    >>> evaluate(3, '+', 3)
    6.0
    >>> evaluate(5, '-', 2)
    3.0
    >>> evaluate(4, '*', 7)
    28.0
    """
    if y == '+':
        return float(x + z )
    elif y == '/':
        return float(x / z)
    elif y == '*':
        return float(x * z)
    elif y== '-':
        return float(x - z)
    else:
        return -1

if __name__ == '__main__':
    calculation = input("")
    x2, y, z2 = calculation.split(" ")
    x1 = int(x2)
    z1 = int(z2)
    print(evaluate(x1, y, z1))