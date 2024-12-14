list1, list2 = map(
    sorted,
    map(list, zip(*[map(int, line.split()) for line in open("input.txt", "r")])),
)
print(f"Part 1: {sum([abs(list2[i] - list1[i]) for i in range(len(list1))])}")
print(f"Part 2: {sum([num*list2.count(num) for num in list1])}")
