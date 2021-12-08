# https://adventofcode.com/2021/day/7

from pathlib import Path
import math
import statistics

path = Path("input.txt")
# path = Path("sample.txt")

with open(path, 'r') as f:
    data = list(map(int, f.readline().strip().split(",")))


def part1(data: list) -> int:
    median = statistics.median(data)
    return int(sum([abs(median-i) for i in data]))


def part2(data: list) -> int:
    mean = statistics.mean(data)
    return int(sum([abs(mean-i)*(abs(mean-i) + 1) / 2 for i in data]))


# Part 1
print(f"Part 1: {part1(data)}")  # -> 345197


# Part 2
print(f"Part 2: {part2(data)}")  # -> 96361606
