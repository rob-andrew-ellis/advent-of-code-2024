def read_data(data_path: str) -> list[list[str]]:
    with open(data_path, "r") as file:
        return [list(line.strip()) for line in file]


def part1(data: list[list[str]]) -> int:
    targets = (("X", "M", "A", "S"), ("S", "A", "M", "X"))
    num_found = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if all([(x + i) < len(data[y]) for i in range(1, 4)]) and (
                (data[y][x], data[y][x + 1], data[y][x + 2], data[y][x + 3]) in targets
            ):
                num_found += 1
            if all([(y + i) < len(data) for i in range(1, 4)]) and (
                (data[y][x], data[y + 1][x], data[y + 2][x], data[y + 3][x]) in targets
            ):
                num_found += 1
            if all(
                [(y + i) < len(data) and (x + i) < len(data[y]) for i in range(1, 4)]
            ) and (
                (
                    data[y][x],
                    data[y + 1][x + 1],
                    data[y + 2][x + 2],
                    data[y + 3][x + 3],
                )
                in targets
            ):
                num_found += 1
            if (all([(y + i) < len(data) for i in range(1, 4)])) and (
                data[y][x],
                data[y + 1][x - 1],
                data[y + 2][x - 2],
                data[y + 3][x - 3],
            ) == ("X", "M", "A", "S"):
                if (x - 1) > 0 or (x - 2) > 0 or (x - 3) > 0:
                    num_found += 1
            if (all([(x + i) < len(data[y]) for i in range(1, 4)])) and (
                data[y][x],
                data[y - 1][x + 1],
                data[y - 2][x + 2],
                data[y - 3][x + 3],
            ) == ("X", "M", "A", "S"):
                if (y - 1) > 0 or (y - 2) > 0 or (y - 3) > 0:
                    num_found += 1

    return num_found


def in_bounds(y: int, x: int, max: int) -> bool:
    return 1 <= y < max - 1 and 1 <= x < max - 1


def part2(data: list[list[str]]) -> int:
    corners = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]

    num_found = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != "A":
                continue
            if in_bounds(y, x, len(data)):
                found = 0
                for corner in corners:
                    if (
                        data[y + corner[0][0]][x + corner[0][1]] == "M"
                        and data[y + corner[1][0]][x + corner[1][1]] == "S"
                    ) ^ (
                        data[y + corner[0][0]][x + corner[0][1]] == "S"
                        and data[y + corner[1][0]][x + corner[1][1]] == "M"
                    ):
                        found += 1
                if found == 2:
                    num_found += 1

    return num_found


if __name__ == "__main__":
    data = read_data("data.txt")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
