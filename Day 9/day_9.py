# https://adventofcode.com/2021/day/9

from pathlib import Path
from math import prod

path = Path("input.txt")
# path = Path("sample.txt")


data = []
with open(path, 'r') as f:
    data = [[int(x) for x in line.strip()] for line in f]

rows = len(data)
cols = len(data[0])


def neigbours(i, j):
    if i > 0:
        pu = data[i-1][j]
    else:
        pu = 9

    if i < rows-1:
        pd = data[i+1][j]
    else:
        pd = 9

    if j > 0:
        pl = data[i][j-1]
    else:
        pl = 9

    if j < cols-1:
        pr = data[i][j+1]
    else:
        pr = 9

    return [pu, pd, pl, pr]


def neigbours_index(p):
    i = p[0]
    j = p[1]
    if i > 0 and i < rows-1 and j > 0 and j < cols-1:
        return [[i+1, j], [i-1, j], [1, j-1], [i, j+1]]
    return None


def part1(data: list) -> int:
    low_points = []

    for i in range(rows):
        for j in range(cols):
            p = data[i][j]
            pu, pd, pl, pr = neigbours(i, j)

            if (p < pu and p < pd and p < pl and p < pr):
                low_points.append(p)

    return sum(low_points) + len(low_points)


def point_hash(point):
    return point[0] + point[1]*100


directions = [
    (-1, 0), (0, 1), (0, -1), (1, 0),
]


def part2(data):

    low_points_locations = []

    for y in range(len(data)):
        for x in range(len(data[0])):
            point = data[y][x]
            is_lowest = True
            for dir in directions:
                dy, dx = dir
                if y+dy in range(len(data)) and x+dx in range(len(data[0])):
                    adjacent = data[y+dy][x+dx]
                    if adjacent <= point:
                        is_lowest = False
                        break

            if is_lowest:
                low_points_locations.append([y, x])

    basins = []

    for start_point in low_points_locations:
        visited = []
        to_visit = [start_point]

        # dont stop until there are no more points to go
        while len(to_visit) > 0:
            current_point = to_visit.pop(0)
            y, x = current_point
            current_point_value = data[y][x]

            # check all the adjacent positions
            for dir in directions:
                dy, dx = dir
                if y+dy in range(len(data)) and x+dx in range(len(data[0])):
                    adjacent = data[y+dy][x+dx]
                    if adjacent < 9 and adjacent >= current_point_value:
                        adjacent_cords = [y+dy, x+dx]

                        # if we found a NEW point to explore
                        if point_hash(adjacent_cords) not in visited:
                            to_visit.append(adjacent_cords)

            # mark as visited
            if point_hash(current_point) not in visited:
                visited.append(point_hash(current_point))

        basins.append(len(visited))

    a, b, c = sorted(basins)[-3:]
    return (a*b*c)


# Part 1
print(f"Part 1: {part1(data)}")  # -> 570

# Part 2
print(f"Part 2: {part2(data)}")  # -> 899392
