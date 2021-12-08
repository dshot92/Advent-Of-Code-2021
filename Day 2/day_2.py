# https://adventofcode.com/2021/day/2

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")

with open(path, "r") as f:
    lines = f.readlines()

data = [l.split() for l in lines]


def part1(data: list) -> int:
    hor_off = 0
    depth_off = 0
    for com in data:
        if com[0] in "forward":
            hor_off += int(com[1])
        if com[0] in "down":
            depth_off += int(com[1])
        if com[0] in "up":
            depth_off -= int(com[1])
    return hor_off * depth_off


def part2(data: list) -> int:
    hor_off = 0
    depth_off = 0
    aim = 0
    for com in data:
        # print(com[0], com[1])
        if com[0] in "forward":
            hor_off += int(com[1])
            depth_off += aim * int(com[1])
        if com[0] in "down":
            aim += int(com[1])
        if com[0] in "up":
            aim -= int(com[1])
    return hor_off * depth_off


print(f"Part 1: {part1(data)}")
print(f"Part 2: {part2(data)}")
