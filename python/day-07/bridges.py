import re
from math import prod


def can_mult(target: int, focus: list[int]) -> bool:
    return all([target % num == 0 for num in focus])


def part1(data: list[list[int]]) -> int:
    total = 0

    for line in data:
        if sum(line[1:]) == line[0] or prod(line[1:]) == line[0]:
            total += line[0]
            data.remove(line)

    print(total)
    print(len(data))


if __name__ == "__main__":
    data = [list(map(int, re.findall(r"\d+", line))) for line in open("input.txt")]
    for line in data:
        if not can_mult(line[0], line[1:]):
            data.remove(line)

    print(len(data))
    part1(data)
