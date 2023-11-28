def pie_percent(n: int) -> int:
    """Precondition: n > 0

    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.

    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """
    return int(100 / n)
    
def triple(n: int) -> int:
    
    return int(n*3)
"""
de functie verdrievoudigd de input
VOORWAARDE: n > 0
>>> triple(4)
12
>>> triple(3)
9
>>> triple(6)
18
"""

        
        

def absdiff(x: int , y: int) -> int:
    """
De functie berekend het verschil tussen de abs waarden
>>> absdiff(3,-9)
12
>>> absdiff(4,4)
0
>>> absdiff (7,1)
6
"""
    verschil = (x-y)
    final_diff = abs(verschil)
   
    
    return int(final_diff)
        



def kmmiles(n: int) -> float:
    """"De functie zet n(kilometers) om naar miles
>>> kmmiles(100)
62.5
>>> kmmiles(60)
37.5
>>> kmmiles (90)
56.25
"""
    miles = (n/1.6)
   
    return float(miles)
    
    


def avg3( x:int , y:int, z:int) -> float:
    
    """"
De functie berekent het gemiddelde van 3 variabelen(x,y,z)
voorbeeld
>>> avg3(1,2,3)
2.0
>>> avg3 (3,3,3)
3.0
>>> avg3(5,5,5)
5.0
"""
    totaal = x+y+z
    return float(totaal / 3)
    


def avg3of4(x: int, y: int, z: int, n: int) -> float:
    """
    De functie selecteert de grootste 3 getallen
    en berekent hier het gemiddelde van.
    input moet 0 > en <=100
    >>> avg3of4(1, 2, 3, 4)
    3.0
    """
    total = x + y + z + n

    total -= min(x, y, z, n)

    avg3 = total / 3

    return avg3