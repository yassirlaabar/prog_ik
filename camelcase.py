def convert(name: str) -> str:
    """
    Converteert een naam van camelCase naar snake_case
    >>> convert("heyHoi")
    'hey_hoi'
    >>> convert("testTest")
    'test_test'
    >>> convert("testHoi")
    'test_hoi'
    """
    snake_case = ""

    for char in name:
        if char.isupper():
            snake_case += "_"
        snake_case += char.lower()
    
    return snake_case


    
if __name__ == '__main__':
    camelcase = input("camelCase:")
    snake_case= convert(camelcase)
    print(f"snake_case {snake_case}")


