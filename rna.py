dnalist = ['A', 'a', 'G', 'g', 'T', 't', 'c', 'C']
def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA string is.
    Accepteert zowel hoofd- als kleine letters.
    >>> check_input('ATGC')
    True
    >>> check_input('hello')
    False
    """
   
    for letter in dna:
        if letter not in 'GCATgcat':
            return False
    return True

def transcribe_dna_to_rna(dna_list: list[str]) -> list[str]:
    """
    Schrijft een lijst met DNA-elementen om naar een lijst met
    RNA-elementen.
    >>> transcribe_dna_to_rna(['C'])
    ['G']
    >>> transcribe_dna_to_rna(['A'])
    ['U']
    """
    rna_list = []
    for dna in dna_list:
        if dna == 'A' or dna  == 'a':
            rna_list.append('U')
        elif dna == 'G' or dna == 'g':
            rna_list.append('C')
        elif dna == 'C' or dna == 'c':
            rna_list.append('G')
        elif dna == 'T' or dna == 't':
            rna_list.append('A')
    return(rna_list)
            

def convert_to_list(dna: str) -> list[str]:
    """
    Converteert de DNA-string naar een lijst met nucleotiden.
    Accepteert zowel hoofd- als kleine letters.
    Uitvoer is alleen hoofdletters.
    >>> convert_to_list('1234')
    ['1', '2', '3', '4']
    >>> convert_to_list('ATCG')
    ['A', 'T', 'C', 'G']
    """
    return list(dna.upper())

def convert_to_string(rna: list[str]) -> str:
    """
    Converteert de RNA-lijst naar string van nucleotiden.
    >>> convert_to_string(['1', '2', '3', '4'])
    '1234'
    >>> convert_to_string(['A', 'T', 'C', 'G'])
    'ATCG'
    """
    return ''.join(rna)
if __name__ == '__main__':
    dna = input("DNALIST: ")
    if check_input(dna):
        dna_list = convert_to_list(dna)
        rna_list = transcribe_dna_to_rna(dna_list)
        rna = convert_to_string(rna_list)
        print(rna)
    else:
        print("That is not a valid DNA string")