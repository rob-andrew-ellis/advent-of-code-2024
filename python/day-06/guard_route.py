import numpy as np
import numpy.typing as npt


# FIX: This shit broke
def read_map(map_path: str) -> npt.NDArray[np.str_]:
    with open(map_path, "r") as file:
        map = [list(line.rstrip()) for line in file]

    return np.array(map)


def part1(map: npt.NDArray[np.str_]) -> int:
    guard_pos = np.where(map == "^")
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = 0

    while all(
        0 <= (guard_pos[0] + steps[direction][0]) < 129
        and 0 <= (guard_pos[1] + steps[direction][1]) < 129
    ):
        if (
            map[
                (guard_pos[0] + steps[direction][0], guard_pos[1] + steps[direction][1])
            ]
            != "#"
        ):
            map[guard_pos] = "X"
            guard_pos = (
                guard_pos[0] + steps[direction][0],
                guard_pos[1] + steps[direction][1],
            )

        elif direction < 3:
            direction += 1
        else:
            direction = 0

    return np.char.count(map, "X").sum()


if __name__ == "__main__":
    map = read_map("map.txt")
    print(map)
    print(part1(map))
