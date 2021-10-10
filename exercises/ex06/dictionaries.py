"""Practice with dictionaries."""

__author__ = "730466264"


# Define your functions below

def main() -> None: 
    dict_1: dict[str, str] = {'a': '1', 'b': '2', 'c': 'x', 'd': 'w'}
    dict_2: dict[str, str] = {'a': 'blue', 'b': 'blue', 'c': 'green', 'd': 'green'}
    list_1: list[str] = []
    print(invert(dict_1))
    print(favorite_color(dict_2))
    print(count(list_1))
    # print_dict(dict_1)
    # print_dict(invert(dict_1))


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    for key in dict_1:
        for inverted_key in invert_dict:
            if dict_1[key] == inverted_key:
                raise KeyError("Two keys will be repeated")
        invert_dict[dict_1[key]] = key
    return invert_dict


def favorite_color(dict_2: dict[str, str]) -> str: 
    favorite_color: str
    dict_count: dict[str, int] = {}
    found: bool = bool(False)

    for key in dict_2: 
        for count_key in dict_count: 
            if dict_2[key] == count_key:
                dict_count[dict_2[key]] += 1
                found = True
        if not found: 
            dict_count[dict_2[key]] = 1 
        found = False
        
    compare_number: int = 0 
    for key in dict_count: 
        if dict_count[key] > compare_number:
            compare_number = dict_count[key]
            favorite_color = key
    return favorite_color


def count(list_1: list[str]) -> dict[str, int]:
    dict_count: dict[str, int] = {}
    i: int = 0
    found: bool = bool(False)

    while i < len(list_1):
        for key in dict_count: 
            if list_1[i] == key:
                dict_count[key] += 1
                found = True
        if not found:
            dict_count[list_1[i]] = 1
        i += 1
        found = False
    return dict_count


def print_dict(dict_1: dict[str, str]) -> None: 
    for key in dict_1:
        print(f"Key: {key} -> Value: {dict_1[key]}")
    
    return None


if __name__ == "__main__":
    main()