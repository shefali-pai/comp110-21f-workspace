"""List utility functions part 2."""

__author__ = "730466264"

# Define your functions below
from typing import List


def main() -> None: 
    """Entry of function."""
    list_1: List[int] = [1, 3, 5]
    list_2: List[int] = [1]
    a_list: List[int] = []
    number_1: int = 1
    number_2: int = 4
    print(only_evens(list_1))
    print(sub(a_list, number_1, number_2))
    print(concat(list_1, list_2))


def only_evens(list_1: List[int]) -> List[int]:
    """Finding evens in a list."""
    i: int = 0
    even_list: List[int] = []

    while i < len(list_1):
        if list_1[i] % 2 == 0:
            even_list.append(list_1[i])
        i += 1
    return even_list


def sub(a_list: List[int], number_1: int, number_2: int) -> List[int]:
    """Making a new list with some list items."""
    new_list: List[int] = []
    empty_list: List[int] = []

    if len(a_list) == 0: 
        return empty_list
    else: 
        if number_1 > len(a_list) - 1: 
            return empty_list
        else: 
            if number_2 <= 0: 
                return empty_list

    if number_1 < 0:
        new_list.append(a_list[0])
    if number_2 > len(a_list):
        new_list.append(a_list[len(a_list) - 1])
    else: 
        new_list.append(a_list[number_1])
        new_list.append(a_list[number_2 - 1])
    
    return new_list


def concat(list_1: List[int], list_2: List[int]) -> List[int]:
    """Putting two lists together."""
    i: int = 0
    concat_list: List[int] = []

    while i < len(list_1):
        concat_list.append(list_1[i])
        i += 1
    
    i = 0
    while i < len(list_2):
        concat_list.append(list_2[i])
        i += 1

    return concat_list


if __name__ == "__main__":
    main()