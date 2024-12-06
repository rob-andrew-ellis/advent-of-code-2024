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
        page_set = set(page)
        changes_needed = any(
            rule[0] in page_set
            and rule[1] in page_set
            and page.index(rule[0]) > page.index(rule[1])
            for rule in rules
        )

        if not changes_needed:
            correct_pages.append(page)
        else:
            incorrect_pages.append(page)

    return sum([page[len(page) // 2] for page in correct_pages]), incorrect_pages


def fix_pages(rules: list[list[int]], pages: list[list[int]]) -> int:
    fixed_pages = []
    while len(pages) > 0:
        for page in pages:
            page_set = set(page)

            changes_made = False
            for rule in rules:
                if (
                    rule[0] in page_set
                    and rule[1] in page_set
                    and page.index(rule[0]) > page.index(rule[1])
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
