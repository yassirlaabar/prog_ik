def calculate_grade(words: int, sentences: int, letters: int) -> float:
    """
    Berekent eerst de waarden L en S gebasseerd op het aantal
    woorden en zinnen. Returnt de grade op basis van deze gegevens.
    >>> calculate_grade(5, 119, 639)
    50
    >>> calculate_grade(20,100,700)
    42
    >>> calculate_grade(10,2,2)
    -16
    """
    L = (letters // words) * 100
    S = (sentences // words) * 100
    return round(0.0588 * L - 0.296 * S - 15.8)
    

    

def coleman_liau(L: float, S: float) -> float:
    """
    Berekent de index (CLI) volgens de Coleman Liau-formule.
    >>> coleman_liau(13,5)
    -17
    >>> coleman_liau(45,76)
    -36
    >>> coleman_liau(10,10)
    -18
    """
    CLI = 0.0588 * L - 0.296 * S - 15.8
    return round(CLI)

if __name__ == '__main__':
    
    text = input("Text: ")

    aantal_zinnen = 0
    for teken in text:
        if  teken == '!' or teken == '?' or teken == '.':
            aantal_zinnen += 1


    aantal_woorden = 0
    for w_space in text:
        if w_space == " ":
            aantal_woorden += 1

    aantal_letters = 0
    for char in text:
        if char.isalpha():
            aantal_letters += 1


    grade_result = calculate_grade(aantal_woorden, aantal_zinnen, aantal_letters)

    if grade_result > 16:
        print('Grade 16+')
    elif grade_result < 1:
        print('Below Grade 1')
    else:
        print(f'Grade {grade_result}')
    

 
