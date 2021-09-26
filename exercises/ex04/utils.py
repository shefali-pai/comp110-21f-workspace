"""List utility functions."""

__author__ = "730466264"

# TODO: Implement your functions here.


def main() -> None: 
    list_1: list[int] = [1, 1, 1, 3, 5]
    list_2: list[int] = [1, 1, 1]
    compare_number: int = 5
    print(1)
    print(all(list_1, compare_number))
    print(is_equal(list_1, list_2))


def all(list_1: list[int], compare_number: int) -> bool:
    i: int = 0
    while i < len(list_1):
        if list_1[i] != compare_number:
            return False
        else: 
            i = i + 1
    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_2):
        if list_1[i] != list_2[i]:
            return False
        else:
            i = i + 1
    return True


if __name__ == "__main__":
    main()