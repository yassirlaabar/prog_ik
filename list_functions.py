def same_first_last(in_list: list[object]) -> bool:
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the
    last.
    
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    """
    last_L = in_list[-1]
    first_L = in_list[0]
    if last_L == first_L:
        return True
    else:
        return False

def is_longer(in_list1: list[object], in_list2: list[object]) -> bool:
    """
    Return True if and only if the length of L1 is longer
    than the length of L2.
    
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    """
    first_list = in_list1
    second_list = in_list2

    if len(first_list) > len(second_list):
        return True
    else:
        return False



