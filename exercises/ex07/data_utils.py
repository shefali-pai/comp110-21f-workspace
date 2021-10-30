"""Utility functions."""

__author__ = "730466264"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(tbl: dict[str, list[str]], rw_nmbr: int) -> dict[str, list[str]]:
    """Creating a dictionary from the table."""
    return_dict: dict[str, list[str]] = {}
    
    if rw_nmbr >= len(tbl):
        return tbl
    for clmn in tbl: 
        n_list: list[str] = []
        i: int = 0
        while i < rw_nmbr: 
            n_list.append(tbl[clmn][i])
            i += 1
        return_dict[clmn] = n_list
    return return_dict


def select(clmn_tbl: dict[str, list[str]], clmn: list[str]) -> dict[str, list[str]]:
    """Creating a table from columns from an original column table."""
    return_dict: dict[str, list[str]] = {}
    for key in clmn:
        return_dict[key] = clmn_tbl[key]
    return return_dict


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Producing a table made out of columns from 2 tables from columns."""
    return_dict: dict[str, list[str]] = {}
    for key in dict_1: 
        return_dict[key] = dict_1[key]
    for key in dict_2:
        if key in return_dict: 
            return_dict[key] += dict_2[key]
        else:
            return_dict[key] = dict_2[key]
    return return_dict


def count(values: list[str]) -> dict[str, int]:
    """Counting the frequency of values."""
    return_dict: dict[str, int] = {}
    for key in values: 
        if key in return_dict: 
            value_present: int = return_dict[key]
            return_dict[key] = value_present + 1
        else: 
            return_dict[key] = 1
    return return_dict