# https://adventofcode.com/2021/day/12

from pathlib import Path
from collections import defaultdict, deque

path = Path("input.txt")
# path = Path("sample.txt")


G = defaultdict(list)
with open(path, "r") as f:
    for line in f:
        a, b = line.strip().split("-")
        G[a].append(b)
        G[b].append(a)

print(G)


def part1(data: list, p1: bool) -> int:
    ans = 0
    start = ("start", set(["start"]), None)
    Q = deque([start])
    while Q:
        curr, small, twice = Q.popleft()
        if curr == "end":
            ans += 1
            continue
        for n in G[curr]:
            if n not in small:
                new_small = set(small)
                if n == n.lower():
                    new_small.add(n)
                Q.append((n, new_small, twice))
            elif n in small and twice is None and n not in ["start", "end"] and not p1:
                Q.append((n, small, n))
    return ans


# Part 1
print(f"Part 1: {part1(G,True)}")  # ->

# Part 2
print(f"Part 2: {part1(G,False)}")  # ->
