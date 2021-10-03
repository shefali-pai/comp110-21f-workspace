"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730466264"

from typing import List
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_even_list() -> None:
    input_list: List[int] = [1, 2, 3, 4, 5, 6]
    even_list: List[int] = [2, 4, 6]
    assert only_evens(input_list) == even_list


def test_only_evens_no_evens() -> None: 
    input_list: List[int] = [1, 3, 5, 7, 9]
    even_list: List[int] = []
    assert only_evens(input_list) == even_list


def test_only_evens_input_empty() -> None: 
    input_list: List[int] = []
    even_list: List[int] = []
    assert only_evens(input_list) == even_list


def test_sub_normal_case() -> None: 
    input_list: List[int] = [1, 2, 3, 4, 5]
    sub_list: List[int] = [2, 3]
    number_1: int = 1
    number_2: int = 3
    assert sub(input_list, number_1, number_2) == sub_list


def test_sub_input_empty() -> None: 
    input_list: List[int] = []
    sub_list: List[int] = []
    number_1: int = 1
    number_2: int = 3
    assert sub(input_list, number_1, number_2) == sub_list


def test_sub_large_boundaries() -> None: 
    input_list: List[int] = [1, 2, 3, 4, 5]
    sub_list: List[int] = [1, 5]
    number_1: int = -1
    number_2: int = 6
    assert sub(input_list, number_1, number_2) == sub_list


def test_concat_empty_list() -> None: 
    input_list: List[int] = []
    input_list_2: List[int] = []
    concat_list: List[int] = []
    assert concat(input_list, input_list_2) == concat_list


def test_concat_normal_case() -> None: 
    input_list: List[int] = [1, 2, 3, 4, 5]
    input_list_2: List[int] = [1, 2, 3]
    concat_list: List[int] = [1, 2, 3, 4, 5, 1, 2, 3]
    assert concat(input_list, input_list_2) == concat_list


def test_concat_empty_first_list() -> None: 
    input_list: List[int] = []
    input_list_2: List[int] = [1, 2, 3]
    concat_list: List[int] = [1, 2, 3]
    assert concat(input_list, input_list_2) == concat_list
