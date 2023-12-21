# This is a sample Python script.
import sys
from pathlib import Path


if __name__ == '__main__':

    # Paths to files with input data
    path_file = Path(sys.argv[1])

    # Process of reading input data
    with open(path_file) as file:
        nums = [int(line.rstrip('\n')) for line in file]

    # Data processing and output
    median = round(sum(nums) / len(nums))

    steps = 0
    for i in nums:
        steps += abs(median - i)

    print(steps)
