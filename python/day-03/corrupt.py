import re


def read_data(data_path: str) -> str:
    with open(data_path, "r") as file:
        return file.read()


def mul(data: str) -> int:
    num_pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    num_pairs = [(int(a), int(b)) for a, b in num_pairs]

    return sum([(a * b) for a, b in num_pairs])


def conditional_mul(data: str) -> int:
    num_pairs = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)

    muls = []
    do = True
    for condition in num_pairs:
        if condition == "do()":
            do = True
        elif condition == "don't()":
            do = False
        elif do:
            muls.append(condition)

    return sum(
        int(a) * int(b) for a, b in [re.findall(r"\d+", multi) for multi in muls]
    )


if __name__ == "__main__":
    print(f"All multiplications = {mul(read_data("data.txt"))}")
    print(f"Conditional multiplications = {conditional_mul(read_data("data.txt"))}")
