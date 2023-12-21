#!/bin/python3
import sys


if __name__ == '__main__':

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = ""
    el = 1
    while True:
        path += str(el)
        tmp = str(el)
        for step in range(m-1):
            if el == n:
                el = 1
            else:
                el += 1
            tmp += str(el)

        # print(f"interval = {tmp}", end="\n")
        if el == 1:
            break

    print(path)



