def read_data(data_path: str) -> list[list[str]]:
    lines = []
    with open(data_path, "r") as file:
        for line in file:
            lines.append(list(line.strip()))

    return lines


data = read_data("data.txt")

# data = [
#     [".", ".", "X", ".", ".", "."],
#     [".", "S", "A", "M", "X", "."],
#     [".", "A", ".", ".", "A", "."],
#     ["X", "M", "A", "S", ".", "S"],
#     [".", "X", ".", ".", ".", "."],
# ]

# data = [
#     ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
#     ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
#     ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
#     ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
#     ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
#     ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
#     ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
#     ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
#     ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
#     ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
# ]

# data = [
#     [".", "M", ".", "S", ".", ".", ".", ".", ".", "."],
#     [".", ".", "A", ".", ".", "M", "S", "M", "S", "."],
#     [".", "M", ".", "S", ".", "M", "A", "A", ".", "."],
#     [".", ".", "A", ".", "A", "S", "M", "S", "M", "."],
#     [".", "M", ".", "S", ".", "M", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["S", ".", "S", ".", "S", ".", "S", ".", "S", "."],
#     [".", "A", ".", "A", ".", "A", ".", "A", ".", "."],
#     ["M", ".", "M", ".", "M", ".", "M", ".", "M", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
# ]

# # Iterate over all of the letters
# num_found = 0
# for y in range(len(data)):
#     for x in range(len(data[y])):
#         # try:
#         #     print("Got: ", (data[y][x], data[y][x - 1], data[y][x - 2], data[y][x - 3]))
#         #     print("Expected: ", ("X", "M", "A", "S"))
#         # except IndexError:
#         #     pass
#         try:
#             if (data[y][x], data[y][x + 1], data[y][x + 2], data[y][x + 3]) == (
#                 "X",
#                 "M",
#                 "A",
#                 "S",
#             ):
#                 num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (data[y][x], data[y][x - 1], data[y][x - 2], data[y][x - 3]) == (
#                 "X",
#                 "M",
#                 "A",
#                 "S",
#             ):
#                 if (x - 1) > 0 or (x - 2) > 0 or (x - 3) > 0:
#                     num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (data[y][x], data[y + 1][x], data[y + 2][x], data[y + 3][x]) == (
#                 "X",
#                 "M",
#                 "A",
#                 "S",
#             ):
#                 num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (data[y][x], data[y - 1][x], data[y - 2][x], data[y - 3][x]) == (
#                 "X",
#                 "M",
#                 "A",
#                 "S",
#             ):
#                 if (y - 1) > 0 or (y - 2) > 0 or (y - 3) > 0:
#                     num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (
#                 data[y][x],
#                 data[y - 1][x - 1],
#                 data[y - 2][x - 2],
#                 data[y - 3][x - 3],
#             ) == ("X", "M", "A", "S"):
#                 if (x - 1) > 0 or (x - 2) > 0 or (x - 3) > 0:
#                     if (y - 1) > 0 or (y - 2) > 0 or (y - 3) > 0:
#                         num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (
#                 data[y][x],
#                 data[y + 1][x + 1],
#                 data[y + 2][x + 2],
#                 data[y + 3][x + 3],
#             ) == ("X", "M", "A", "S"):
#                 num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (
#                 data[y][x],
#                 data[y + 1][x - 1],
#                 data[y + 2][x - 2],
#                 data[y + 3][x - 3],
#             ) == ("X", "M", "A", "S"):
#                 if (x - 1) > 0 or (x - 2) > 0 or (x - 3) > 0:
#                     num_found += 1
#         except IndexError:
#             pass
#         try:
#             if (
#                 data[y][x],
#                 data[y - 1][x + 1],
#                 data[y - 2][x + 2],
#                 data[y - 3][x + 3],
#             ) == ("X", "M", "A", "S"):
#                 if (y - 1) > 0 or (y - 2) > 0 or (y - 3) > 0:
#                     num_found += 1
#         except IndexError:
#             pass


def in_bounds(y: int, x: int, max) -> bool:
    return 1 <= y < max - 1 and 1 <= x < max - 1


corners = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]

num_found = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] != "A":
            continue
        if in_bounds(y, x, len(data)):
            found = 0
            for corner in corners:
                if data[y + corner[0][0]][x + corner[0][1]] == "M":
                    if data[y + corner[1][0]][x + corner[1][1]] == "S":
                        found += 1
                elif data[y + corner[0][0]][x + corner[0][1]] == "S":
                    if data[y + corner[1][0]][x + corner[1][1]] == "M":
                        found += 1
            if found == 2:
                num_found += 1


print(num_found)
