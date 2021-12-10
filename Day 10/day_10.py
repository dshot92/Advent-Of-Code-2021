# https://adventofcode.com/2021/day/10

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")


data = []
with open(path, 'r') as f:
    data = f.readlines()


def part1(data: list) -> int:
    result = 0
    for line in data:
        queue = []
        for c in line.strip(''):
            if c in ["(", "[", "{", "<"]:
                queue.append(c)
            elif c == ")":
                if queue[-1] != "(":
                    result += 3
                    break
                else:
                    queue.pop()
            elif c == "]":
                if queue[-1] != "[":
                    result += 57
                    break
                else:
                    queue.pop()
            elif c == "}":
                if queue[-1] != "{":
                    result += 1197
                    break
                else:
                    queue.pop()
            elif c == ">":
                if queue[-1] != "<":
                    result += 25137
                    break
                else:
                    queue.pop()
    return result


def part2(data):
    result = 0
    score = []
    d = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in data:
        queue = []
        for c in line.strip(''):
            bad = False
            if c in ["(", "[", "{", "<"]:
                queue.append(c)
            elif c == ")":
                if queue[-1] != "(":
                    result += 3
                    bad = True
                    break
                else:
                    queue.pop()
            elif c == "]":
                if queue[-1] != "[":
                    result += 57
                    bad = True
                    break
                else:
                    queue.pop()
            elif c == "}":
                if queue[-1] != "{":
                    result += 1197
                    bad = True
                    break
                else:
                    queue.pop()
            elif c == ">":
                if queue[-1] != "<":
                    result += 25137
                    bad = True
                    break
                else:
                    queue.pop()

    result = 0
    if not bad:
        for p in queue[::-1]:
            score.append(d[p])

    for p in score:
        result = result*5 + p
    scores.append(result)
    return scores[len(scores)//2]


# Part 1
print(f"Part 1: {part1(data)}")  # -> 319329

# Part 2
print(f"Part 2: {part2(data)}")  # -> 3515583998
