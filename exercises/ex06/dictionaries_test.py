"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730466264"


from exercises.ex06.dictionaries import invert


def test_invert_empty_dictionary() -> None:
    """Testing if empty dictionaries are produced."""
    input_dictionary: dict[str, str] = {}
    output_dictionary: dict[str, str] = {}
    assert invert(input_dictionary) == output_dictionary