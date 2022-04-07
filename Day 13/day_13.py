# https://adventofcode.com/2021/day/13

from pathlib import Path

path = Path("input.txt")
path = Path("sample.txt")


data = []
X = 0
Y = 0
x = []
y = []
commands = []
with open(path, "r") as f:
    for line in f:
        if "," in line:
            line = line.strip().split(",")
            x.append(int(line[0]))
            y.append(int(line[0]))
            data.append([int(line[0]), int(line[1])])
        elif "fold" in line:
            line = line.replace("fold along ", "")
            line = line.strip().split("=")
            commands.append([line[0], line[1]])
    X = max(x)
    Y = max(y)

grid = [X]
for p in data:
    grid[p[0]][p[1]] = 1

print(data)
print(X, Y)
print(commands)


def fold(data, commands):
    for command in commands:
        if command[0] == "x":
            data = fold_x(data, command[1])
        elif command[0] == "y":
            data = fold_y(data, command[1])
    return data


def fold_x(data, x):
    for y in range(Y):
        for x_ in range(X):
            if x_ == int(x):
                data[y][x_] = 1
            else:
                data[y][x_] = 0
    return data


def part1(data: list) -> int:
    pass


def part2(data):
    pass


# Part 1
print(f"Part 1: {part1(data)}")  # ->

# Part 2
print(f"Part 2: {part2(data)}")  # ->
