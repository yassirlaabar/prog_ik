Board = list[list[int]]
row1 = board[0]
row2 = board[1]
row3 = board[2]
col1 = [board[0][0], board[1][0], board
[2][0]]
col2 = [board[0][1], board[1][1], board
[2][1]]
col3 = [board[0][2], board[1][2], board
[2][2]]
def is_won(board: Board) -> bool:
    """
    Controleert of het bord in een winnende configuratie staat. Geeft True als
    de configuratie winnend is, False als dat niet het geval is.
    """
    
    if board == [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0 ]
    ]:
        return True
    else:
        return False
    

def move_tile(board: Board, tile: int) -> bool:
    """
    Als de te verplaatsten tegel verplaatsbaar is: schuift de tegel in de
    configuratie van het bord en geeft True. Als dat niet het geval is, blijft
    het bord in de oorspronkelijke configuratie en functie geeft False.
    """
# manier vinden om te verplaatsen Gevonden ✅
# eerst checken of die in dezelfde row/ column zit, daarna ook replace
# als die in dezelfde row/ column zit, dan verplaatsen
# als die niet in dezelfde row/ column zit, dan niet verplaatsen
if tile in row1 or tile in row2 or tile in row3:
    if tile in row1:
        row1.remove(tile)
        row1.append(0)
    if 0 in row1 :
        row1.remove(0)
        row1.append(tile)
        return True
    elif 0 in row1 and col2:
        row1.remove(0)
        row1.append(tile)
        return True
    
    
    if is_valid_move == True:

            
    

    

def print_board(board: Board) -> None:
    """
    Print alle rijen van het bord onder elkaar. Het format is zoals in de
    voorbeelden onderaan de opdracht.
    """
    # hoort niks te returnen, dus hier hoort het bord gemaakt te worden??
    for row in board:
        print(row)
    


def create_board() -> Board:
    """
    Initialiseert een bord van formaat 4 x 4.
    Sorteert de nummers op aflopende volgorde van links boven naar rechts beneden.
    De volgorde van de tegels 1 en 2 is verwisseld.
    """
    

    Board = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]]
    for row in Board:
        print(row)   
    
    for col in range(4):
        column = [row[col] for row in Board]
        
    return Board

    
    

def get_valid_moves(board: Board) -> list[int]:
    """
    Genereert een lijst met tegels die door de speler kunnen worden geschoven.
    """
    valid_moves = []
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if is_valid_move(board, row, col):
                valid_moves.append(board[row][col])
    
    return valid_moves

def is_valid_move(board: Board, row: int, col: int) -> bool:
    """
    Controleert of de tegel op de gegeven rij en kolom kan worden geschoven.
    """
    
    


        


if __name__ == '__main__':
    print("Welkom bij de schuifpuzzel!")
    board = create_board()
    while not is_won(board):
        print_board(board)
        tile = input("Tegel die je wil schuiven: ")
        valid = move_tile(board, int(tile))
        if not valid:
            print("Deze tegel kan je niet schuiven.")
    print("Gefeliciteerd, je hebt de schuifpuzzel opgelost!")
