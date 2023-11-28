import doctest

def number_of_Os(x: str) -> int:
    """
    De functie kijkt hoe vaak 'o' voorkomt in x
    >>> number_of_Os('top')
    1
    >>> number_of_Os('test')
    0
    
    """
    number_Os = x.count('o')
    return number_Os
    
def first_O (x:str) -> int:
    """
    de functie bepaalt de plaats vd letter o
    >>> first_O('test')
    -1
    >>> first_O('prima')
    -1
    """
    place_o = x.find('o')
    return place_o

def number_of_letters(x: str , y:str) -> int:
    """
    de functie telt hoevaak y voorkomt in x
    >>> number_of_letters('test' , 'e')
    1
    >>> number_of_letters('hoi' , 'h')
    1
    """
    input_str = x.count(y)
    return input_str

def where_letter(x: str , z:str) -> int:
    """
    de functie kijkt waar z voorkomt in x
    >>> where_letter('hoi' , 'e')
    -1
    >>> where_letter('top' , 'o')
    1
    """
    where_y = x.find(z)
    return where_y
    
def total_occurrences(s1: str, s2: str, ch: str) -> int:
    """
    Return the total number of times that ch occurs in s1 and s2.
        
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    strings = (s1+s2)
    total_number = strings.count(ch)
    return total_number

if __name__ == "__main__":
    doctest.testmod()
