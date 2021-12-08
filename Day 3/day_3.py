# https://adventofcode.com/2021/day/4

from pathlib import Path
import collections

path = Path("input.txt")
# path = Path("sample.txt")

data = open(path).read().splitlines()


def part1(data: list) -> int:
    gamma = []
    epsilon = []
    for i in range(len(data[0])):
        cntr = collections.Counter([r[i] for r in data])
        gamma.append('1' if cntr['1'] > cntr['0'] else '0')
        epsilon.append('0' if cntr['1'] > cntr['0'] else '1')
    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)
    return gamma * epsilon


def part2(data: list):
    gamma = data[::]
    for i in range(len(data[0])):
        most = collections.Counter([r[i] for r in gamma])
        most = '1' if most['1'] >= most['0'] else '0'
        gamma = list(filter(lambda x: x[i] == most, gamma))
        if len(gamma) == 1:
            break

    epsilon = data[::]
    for i in range(len(data[0])):
        least = collections.Counter([r[i] for r in epsilon])
        least = '0' if least['1'] >= least['0'] else '1'
        epsilon = list(filter(lambda x: x[i] == least, epsilon))
        if len(epsilon) == 1:
            break

    epsilon_rate = int(epsilon[0], 2)
    gamma_rate = int(gamma[0], 2)
    return gamma_rate * epsilon_rate


# Part 1
print(f"Part 1: {part1(data)}")

# Part 2
print(f"Part 2: {part2(data)}")
