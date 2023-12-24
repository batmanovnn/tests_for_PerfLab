#!/bin/python3
import json
import sys
from pathlib import Path


def parse(obj, obj2):
    for item in obj:
        print(item)
        if item.get('value') is not None:
            item.update({'value': find_value(item.get('id'), obj2)})
            print(f"id = {item.get('id')}, value = {item.get('value')}")
        if item.get('values') is not None:
            parse(item.get('values'), obj2)


def find_value(id, obj):
    for item in obj:
        if item.get('id') == id:
            return item.get('value')


if __name__ == '__main__':

    # Paths to files with input data
    path_tests = Path(sys.argv[1])
    path_values = Path(sys.argv[2])

    # Process of reading input data
    with open(path_tests) as file:
        tests = json.load(file)

    with open(path_values) as file:
        values = json.load(file)

    # Data processing and output
    parse(tests.get('tests'), values.get('values'))

    # Output result to report.json file:
    with open("report.json", "w") as file:
        json.dump(tests, file, indent=2)

