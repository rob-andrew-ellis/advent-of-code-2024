import pandas as pd

data = pd.read_csv("lists.csv")

list1 = data["list1"].tolist()
list2 = data["list2"].tolist()

list1 = sorted(list1)
list2 = sorted(list2)

distances = []

for i in range(len(list1)):
  distances.append(abs(list2[i] - list1[i]))

print(f"The total distance between the lists is {sum(distances)}")