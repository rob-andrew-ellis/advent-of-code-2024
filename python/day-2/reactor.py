def read_reports(file_path: str) -> list[list[int]]:
    all_reports = []

    with open(file_path, "r") as file:
        for line in file:
            record = list(map(int, line.split(" ")))

            all_reports.append(record)

    return all_reports


def check_safety(all_reports: list[list[int]]) -> int:
    num_safe = 0

    for report in all_reports:
        differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]

        if all([n > 0 for n in differences]) or all([n < 0 for n in differences]):
            if all([(abs(n) >= 1 and abs(n) <= 3) for n in differences]):
                num_safe += 1

    return num_safe


def check_safety2(all_reports: list[list[int]]) -> int:
    def is_valid_sequence(report: list[int]) -> bool:
        is_ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        is_descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))

        differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]

        return (is_ascending or is_descending) and all(
            1 <= diff <= 3 for diff in differences
        )

    num_safe = 0

    for report in all_reports:
        if is_valid_sequence(report):
            num_safe += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]

            if is_valid_sequence(modified_report):
                num_safe += 1
                break

    return num_safe


def problem_dampener(all_reports: list[list[int]]) -> list[list[int]]:
    for report in all_reports:
        differences = [report[i] - report[i + 1] for i in range(len(report) - 1)]

        num_bad = 0
        for i in differences[:]:
            if (abs(differences[i]) < 1 or abs(differences[i]) > 3) and num_bad < 1:
                report.pop(i + 1)
                num_bad += 1
            elif (
                (differences[i] > 0 and differences[i + 1] < 0)
                or (differences[i] < 0 and differences[i + 1] > 0)
            ) and num_bad < 1:
                report.pop(i + 1)
                num_bad += 1

    return all_reports


if __name__ == "__main__":
    all_reports = read_reports("data.txt")
    # print(check_safety(all_reports))
    # print(check_safety(problem_dampener(all_reports)))
    print(check_safety2(all_reports))
