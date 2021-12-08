# https://adventofcode.com/2021/day/1

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")

data = list(map(int, open(path)))


def part1(data: list) -> int:
    inc = 0
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            inc += 1
    return inc


def part2(data: list) -> int:
    inc = 0
    for i in range(len(data)-3):
        wa = data[i] + data[i+1] + data[i+2]
        wb = data[i+1] + data[i+2] + data[i+3]
        if wa < wb:
            inc += 1
    return inc


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
