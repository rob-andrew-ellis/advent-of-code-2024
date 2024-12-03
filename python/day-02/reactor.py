def read_reports(file_path: str) -> list[list[int]]:
    all_reports = []

    with open(file_path, "r") as file:
        for line in file:
            record = list(map(int, line.split(" ")))

            all_reports.append(record)

    return all_reports


def is_safe(report: list[int]) -> bool:
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    return (all(n > 0 for n in diffs) or all(n < 0 for n in diffs)) and all(
        1 <= abs(n) <= 3 for n in diffs
    )


def problem_dampener(all_reports: list[list[int]]) -> int:
    num_safe = 0

    for report in all_reports:
        if is_safe(report):
            num_safe += 1
            continue

        for i in range(len(report)):
            modified_report = report.copy()
            modified_report.pop(i)

            if is_safe(modified_report):
                num_safe += 1
                break

    return num_safe


if __name__ == "__main__":
    all_reports = read_reports("data.txt")
    print(f"Part 1: {len([x for x in filter(is_safe, all_reports)])}")
    print(f"Part 2: {problem_dampener(all_reports)}")
