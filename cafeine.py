
def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Na het beantwoorden van de vragen, wordt de hoeveelheid cafeine berekend.
    
    >>> calculate_cafeine(3,3,3,3)
    765
    >>> calculate_cafeine(1,1,1,1)
    255
    """
    total_mg_coffee = (coffee * 90)
    total_mg_tea = (tea * 45)
    total_mg_energy = (energy * 80)
    total_mg_cola = (cola * 40)
   
    total_cafeine = int(total_mg_coffee + total_mg_tea + total_mg_energy + total_mg_cola)
    return int(total_cafeine)
    

if __name__ == '__main__':
    coffee = int(input("Hoeveel koppen koffie?"))
    tea = int(input("Hoeveel koppen thee?"))
    energy = int(input("Hoeveel energiedrankjes?"))
    cola = int(input("hoeveel glazen cola?"))
    result = calculate_cafeine(coffee, tea, energy , cola)
    print(f"je krijgt",result,"mg cafeine binnen")