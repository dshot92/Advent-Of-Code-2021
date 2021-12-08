# https://adventofcode.com/2021/day/8

from pathlib import Path

path = Path("input.txt")
# path = Path("sample.txt")


def parse_input():
    data = []
    with open(path, 'r') as f:
        for line in f:
            inp, out = line.split(" | ")
            inp, out = inp.split(), out.split()
            data.append((inp, out))
    return data


def part1(data: list) -> int:
    count = 0
    for _, out in data:
        for seg in out:
            count += len(seg) in [2, 4, 3, 7]
    return count


def decode_dictionary(inp):
    digits = {}
    five_len, six_len = [], []

    for digit in inp:
        if len(digit) == 2:
            digits["1"] = set(digit)
        elif len(digit) == 4:
            digits["4"] = set(digit)
        elif len(digit) == 3:
            digits["7"] = set(digit)
        elif len(digit) == 7:
            digits["8"] = set(digit)
        elif len(digit) == 5:
            five_len.append(set(digit))
        elif len(digit) == 6:
            six_len.append(set(digit))

    for digit in five_len:
        # 2, 3, 5
        if len(digit & digits["1"]) and len(digit & digits["4"]) == 2:
            digits["2"] = digit
        elif len(digit & digits["7"]) == 3:
            digits["3"] = digit
        elif len(digit & digits["1"]) == 1 and len(digit & digits["4"]) == 3:
            digits["5"] = digit

    for digit in six_len:
        # 6, 9, 0
        if len(digit & digits["1"]) == 1:
            digits["6"] = digit
        elif len(digit & digits["4"]) == 4:
            digits["9"] = digit
        elif len(digit & digits["4"]) == 3:
            digits["0"] = digit

    decoded = {"".join(sorted(v)): k for k, v in digits.items()}
    return decoded


def part2(problem):
    sum = 0

    for inp, out in problem:
        decoded = decode_dictionary(inp)
        result = []
        for digit in out:
            digit = "".join(sorted(digit))
            result.append(decoded[digit])
        sum += int("".join(result))
    return sum


data = parse_input()

# Part 1
print(f"Part 1: {part1(data)}")  # -> 548


# Part 2
print(f"Part 2: {part2(data)}")  # -> 1074888
