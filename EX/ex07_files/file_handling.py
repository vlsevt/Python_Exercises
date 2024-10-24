"""File handling."""
import csv
import re
from datetime import datetime


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    row_list = []
    with open(filename) as file:
        for line in file.readlines():
            row_list.append(line.replace("\n", ""))
        return row_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    row_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row_list.append(row)
    return row_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        if len(lines) != 0:
            for line in range(len(lines) - 1):
                file.write(f"{lines[line]}\n")
            file.write(lines[-1])


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    dic = {}
    dates = read_file_contents_to_list(dates_filename)
    towns = read_file_contents_to_list(towns_filename)
    for i in dates:
        name = i[0:i.index(":")]
        date = f"{i[i.index(':') + 1:-1]}{i[-1]}"
        town = "-"
        for element in towns:
            if name in element:
                town = f"{element[element.index(':') + 1:-1]}{element[-1]}"
        if name not in dic:
            dic[name] = list()
            dic[name].append(town)
            dic[name].append(date)
    for i in towns:
        name = i[0:i.index(":")]
        town = f"{i[i.index(':') + 1:-1]}{i[-1]}"
        date = "-"
        for element in dates:
            if name in element:
                date = f"{element[element.index(':') + 1:-1]}{element[-1]}"
        if name not in dic:
            dic[name] = list()
            dic[name].append(town)
            dic[name].append(date)
    with open(csv_output_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['name', 'town', 'date'])
        for row in dic:
            csv_writer.writerow([row, dic[row][0], dic[row][1]])


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """Read csv file into list of dictionaries."""
    file = read_csv_file(filename)
    list_of_dicts = []
    dic = {}
    for element in range(1, len(file)):
        for num in range(len(file[0])):
            dic[file[0][num]] = file[element][num]
        list_of_dicts.append(dic)
        dic = {}
    return list_of_dicts


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    first_row = []
    row_list = []
    for dic in data:
        for element in dic.keys():
            if element not in first_row:
                first_row.append(element)
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        if data:
            csv_writer.writerow(first_row)
            for dic in data:
                for i in first_row:
                    if i in dic:
                        row_list.append(dic[i])
                    else:
                        row_list.append("")
                csv_writer.writerow(row_list)
                row_list = []


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise, the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    list_of_dicts = read_csv_file_into_list_of_dicts(filename)
    temporary_int_list = []
    temporary_date_list = []
    if list_of_dicts:
        for i in range(len(list(list_of_dicts[0].keys()))):
            check_column(list_of_dicts, i, temporary_int_list, temporary_date_list)
            for dic in list_of_dicts:
                if len(temporary_int_list) == len(list_of_dicts):
                    if list(dic.values())[i] is not None:
                        dic[list(dic.keys())[i]] = int(list(dic.values())[i])
                if len(temporary_date_list) == len(list_of_dicts):
                    if list(dic.values())[i] is not None and list(dic.values())[i] and list(dic.values())[i].isdigit() is False:
                        dic[list(dic.keys())[i]] = datetime.strptime(list(dic.values())[i], "%d.%m.%Y").date()
            temporary_int_list = []
            temporary_date_list = []
    return list_of_dicts


def check_column(list_of_dicts: list, i: int, temporary_int_list: list, temporary_date_list: list):
    """Check if all values are numbers or dates."""
    for dic in list_of_dicts:
        if (list(dic.values())[i].isdigit()) or (list(dic.values())[i] == '-'):
            temporary_int_list.append(list(dic.values())[i])
        if (re.findall(r"\d{2}\.\d{2}\.\d{4}", list(dic.values())[i])) or (
                list(dic.values())[i] == '-'):
            temporary_date_list.append(list(dic.values())[i])
        if list(dic.values())[i] == '-':
            dic[list(dic.keys())[i]] = None
