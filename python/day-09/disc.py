import time


def part1(result: list[int | str]) -> int:
    dot_id = result.index(".")

    for i in range(len(result) - 1, -1, -1):
        if dot_id == -1 or dot_id >= i:
            break

        result[i], result[dot_id] = result[dot_id], result[i]

        while dot_id < len(result) and result[dot_id] != ".":
            dot_id += 1

    return sum([num * i for i, num in enumerate(result) if isinstance(num, int)])


if __name__ == "__main__":
    start_time = time.time()

    data = list(map(int, open("input.txt", "r").read().strip()))

    result = [
        i - i // 2 if i % 2 == 0 else "."
        for i, num in enumerate(data)
        for _ in range(num)
    ]
    print(part1(result))
    print(f"\nSolution took: {round((time.time() - start_time) * 1000, 2)}ms")
