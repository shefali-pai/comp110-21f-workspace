"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730466264"


from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_empty_dictionary() -> None:
    """Testing if empty dictionaries are produced."""
    input_dictionary: dict[str, str] = {}
    output_dictionary: dict[str, str] = {}
    assert invert(input_dictionary) == output_dictionary


def test_invert_regular_case() -> None: 
    """Testing if the code works regularly."""
    input_dictionary: dict[str, str] = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    output_dictionary: dict[str, str] = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
    assert invert(input_dictionary) == output_dictionary


def test_invert_repeat_case() -> None: 
    """Testing if the code works regularly."""
    input_dictionary: dict[str, str] = {'apple': 'banana', 'broccoli': 'carrot'}
    output_dictionary: dict[str, str] = {'banana': 'apple', 'carrot': 'broccoli'}
    assert invert(input_dictionary) == output_dictionary


def test_favorite_color_empty() -> None: 
    """Testing with empty dictionaries."""
    input_dictionary: dict[str, str] = {'a': 'blue', 'b': 'red', 'c': 'green'}
    output: str = "blue"
    assert favorite_color(input_dictionary) == output


def test_favorite_color_regular_case() -> None: 
    """Testing with regular dictionaries."""
    input_dictionary: dict[str, str] = {'a': 'red', 'b': 'blue', 'c': 'blue'}
    output: str = "blue"
    assert favorite_color(input_dictionary) == output


def test_favorite_color_repeat_case() -> None: 
    """Testing with a repeat case."""
    input_dictionary: dict[str, str] = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue'}
    output: str = "red"
    assert favorite_color(input_dictionary) == output


def test_count_empty_case() -> None: 
    """Testing with an empty list and dictionary."""
    input_list: list[str] = []
    output_dictionary: dict[str, int] = {}
    assert count(input_list) == output_dictionary


def test_count_regular_case() -> None: 
    """Testing with a regular case."""
    input_list: list[str] = ["blue", "blue", "green"]
    output_dictionary: dict[str, int] = {'blue': 2, 'green': 1}
    assert count(input_list) == output_dictionary


def test_count_repeat_case() -> None:
    """Testing with multiple same colors."""
    input_list: list[str] = ["green", "green", "blue", "blue"]
    output_dictionary: dict[str, int] = {'green': 2, 'blue': 2}
    assert count(input_list) == output_dictionary