# https://adventofcode.com/2021/day/11

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")


data = []
with open(path, "r") as f:
    for line in f:
        data.append([int(x) for x in line.strip()])

R = len(data)
C = len(data[0])
ans = 0


def flash(r, c):
    global ans
    ans += 1
    data[r][c] = -1
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and data[rr][cc] != -1:
                data[rr][cc] += 1
                if data[rr][cc] >= 10:
                    flash(rr, cc)


def print_board():
    for r in range(R):
        for c in range(C):
            print(data[r][c], end="")
        print()


def part1(data: list):
    global ans
    for _ in range(100):
        for r in range(R):
            for c in range(C):
                data[r][c] += 1
        for r in range(R):
            for c in range(C):
                if data[r][c] == 10:
                    flash(r, c)
        done = True
        for r in range(R):
            for c in range(C):
                if data[r][c] == -1:
                    data[r][c] = 0
    return ans


def part2(data: list):
    t = 0
    while True:
        t += 1
        for r in range(R):
            for c in range(C):
                data[r][c] += 1
        for r in range(R):
            for c in range(C):
                if data[r][c] == 10:
                    flash(r, c)

        done = True
        for r in range(R):
            for c in range(C):
                if data[r][c] == -1:
                    data[r][c] = 0
                else:
                    done = False
        if done:
            return t


# Part 1
# print(f"Part 1: {part1(data)}")  # -> 1694

# Part 2
print(f"Part 2: {part2(data)}")  # -> 346
