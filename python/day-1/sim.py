import pandas as pd

data = pd.read_csv("lists.csv")

list1 = data["list1"].tolist()
list2 = data["list2"].tolist()

list1 = sorted(list1)
list2 = sorted(list2)

for i in range(len(list1)):
  number_of_appearances = 0

  for j in range(len(list2)):
    if list1[i] == list2[j]:
      number_of_appearances += 1
  
  list1[i] *= number_of_appearances

print(f"The similarity score is {sum(list1)}")