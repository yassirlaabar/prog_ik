import string

POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
Alphabet = string.ascii_lowercase

def compute_score(word: str) -> int:
    """
    Calculate and return the score for the word.
    >>> compute_score('hoi')
    6
    >>> compute_score('hey')
    9
    >>> compute_score('doei')
    5
    """
    score = 0
    for letter in word.lower():
        
        for i, alpha_letter in enumerate(Alphabet):
            if letter == alpha_letter:
                score += POINTS[i]
                break

    return score

if __name__ == '__main__':
    speler_1 = input("Speler 1:")
    speler_2 = input("Speler 2:")

    score_1 = compute_score(speler_1)
    score_2 = compute_score(speler_2)


    if score_1 > score_2:
        print("Speler 1 wint!")
    elif score_2 > score_1:
        print("Speler 2 wint!")
    else:
        print("Gelijkspel!")
