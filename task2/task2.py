#!/bin/python3
import sys
from pathlib import Path


if __name__ == '__main__':

    # Paths to files with input data
    path_file1 = Path(sys.argv[1])
    path_file2 = Path(sys.argv[2])

    # Process of reading input data
    with open(path_file1) as file1:
        center = list(map(float, file1.readline().split(' ')))
        r = float(file1.readline())

    with open(path_file2) as file2:
        dots = [list(map(float, line.rstrip('\n').split(' '))) for line in file2]

    # Data processing and output
    for dot in dots:
        tmp = pow(dot[0] - center[0], 2) + pow(dot[1] - center[1], 2)
        if tmp == pow(r, 2):
            print(f"0", end="\n")
        if tmp < pow(r, 2):
            print(f"1", end="\n")
        if tmp > pow(r, 2):
            print(f"2", end="\n")
