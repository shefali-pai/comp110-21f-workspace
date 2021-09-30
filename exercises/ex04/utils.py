"""List utility functions."""

__author__ = "730466264"

# TODO: Implement your functions here.

from typing import List


def main() -> None:
    """Where all the functions are being called."""
    list_1: List[int] = []
    list_2: List[int] = []
    compare_number: int = 2
    print(all(list_1, compare_number))
    print(is_equal(list_1, list_2))
    print(max(list_1))


def all(list_1: list[int], compare_number: int) -> bool:
    """Comparing a number to a list to see if the list is all the same number."""
    i: int = 0
    if len(list_1) == 0:
        return False
    while i < len(list_1):
        if list_1[i] != compare_number:
            return False
        else: 
            i = i + 1
    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Seeing if two lists are equal to each other."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_2):
        if list_1[i] != list_2[i]:
            return False
        else:
            i = i + 1
    return True


def max(list_1: list[int]) -> int:
    """Finding the max value in the list."""
    i: int = 1
    max_int: int
    if len(list_1) == 0:
        raise ValueError("max() arg is an empty List")
    max_int = list_1[0]
    while i < len(list_1):
        if list_1[i] > max_int:
            max_int = list_1[i]
        i = i + 1
    return max_int


if __name__ == "__main__":
    main()