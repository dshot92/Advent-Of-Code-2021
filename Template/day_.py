# https://adventofcode.com/2021/day/

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")


data = []
with open(path, 'r') as f:
    data = f.readlines()
    # data = [[int(x) for x in line.strip()] for line in f]


def part1(data: list) -> int:
    pass


def part2(data):
    pass


# Part 1
print(f"Part 1: {part1(data)}")  # ->

# Part 2
print(f"Part 2: {part2(data)}")  # ->
