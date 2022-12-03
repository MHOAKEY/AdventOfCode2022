rucksack = []

with open("rucksacks.txt") as f:
    for each in f:
        rucksack.append(each.strip())

one = "vJrwpWtwJgWr"
two = "hcsFMMfFFhFp"
list1 = []
list2 = []

match = []

for char in one:
    list1.append(char)

for char in two:
    list2.append(char)

for element in list1:
    if element in list2:
        match.append(element)

print(match)