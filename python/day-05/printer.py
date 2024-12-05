def read_data(
    rules_path: str, pages_path: str
) -> tuple[list[list[int]], list[list[int]]]:
    with open(rules_path, "r") as file:
        rules = [list(map(int, line.split("|"))) for line in file]

    with open(pages_path, "r") as file:
        pages = [list(map(int, line.split(","))) for line in file]

    return rules, pages


def find_correct_pages(
    rules: list[list[int]], pages: list[list[int]]
) -> tuple[int, list[list[int]]]:
    correct_pages, incorrect_pages = [], []
    for page in pages:
        changes_made = False
        for i, number in enumerate(page):
            for rule in rules:
                if rule[1] == number and (rule[0] in page and page.index(rule[0]) > i):
                    changes_made = True
                    break
            if changes_made:
                break

        if not changes_made:
            correct_pages.append(page)
        else:
            incorrect_pages.append(page)

    return (sum([page[len(page) // 2] for page in correct_pages]), incorrect_pages)


def fix_pages(rules: list[list[int]], pages: list[list[int]]) -> int:
    fixed_pages = []
    while len(pages) > 0:
        for page in pages:
            changes_made = False
            for i, number in enumerate(page):
                for rule in rules:
                    if rule[1] == number and (
                        rule[0] in page and page.index(rule[0]) > i
                    ):
                        page[page.index(rule[0])], page[page.index(rule[1])] = (
                            page[page.index(rule[1])],
                            page[page.index(rule[0])],
                        )
                        changes_made = True
            if not changes_made:
                fixed_pages.append(page)
                pages.remove(page)

    return sum([page[len(page) // 2] for page in fixed_pages])


if __name__ == "__main__":
    rules, pages = read_data("rules.txt", "pages.txt")
    correct_sum, incorrect_pages = find_correct_pages(rules, pages)
    print(f"Sum of middle values for correct pages: {correct_sum}")
    print(f"Sum of middle values for fixed pages {fix_pages(rules, incorrect_pages)}")
