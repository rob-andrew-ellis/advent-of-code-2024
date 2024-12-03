from pathlib import Path

import pandas as pd


def read_data(data_path: Path) -> tuple[list[int], list[int]]:
    """Reads the list data from lists.csv

    Args:
        data_path: Path to file containing the lists

    Returns:
        The data in the form of two lists
    """
    data = pd.read_csv(data_path)

    list1 = data["list1"].tolist()
    list2 = data["list2"].tolist()

    list1 = sorted(list1)
    list2 = sorted(list2)

    return list1, list2


def get_distance(list1: list[int], list2: list[int]) -> int:
    """Gets the absolute distance between location ids in the given lists

    Args:
        list1: First list of location IDs
        list2: Second list of location IDs

    Returns:
        Distance between location IDs
    """
    distances = []

    for i in range(len(list1)):
        distances.append(abs(list2[i] - list1[i]))

    return sum(distances)


def get_similarity_score(list1: list[int], list2: list[int]) -> int:
    """Gets the similarity between the lists by getting the total sum of list1 where
       each instance in list1 is multiplied by the number of occurances in list 2

    Args:
        list1: First list of location IDs
        list2: Second list of location IDs

    Returns:
        Similarity score between the lists
    """
    for i in range(len(list1)):
        number_of_appearences = 0

        for j in range(len(list2)):
            if list1[i] == list2[j]:
                number_of_appearences += 1

        list1[i] *= number_of_appearences

    return sum(list1)


if __name__ == "__main__":
    list1, list2 = read_data(Path("lists.csv"))

    print(f"The total distance between the lists is {get_distance(list1, list2)}")
    print(f"The similarity score is {get_similarity_score(list1, list2)}")

