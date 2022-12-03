# one = "vJrwpWtwJgWr"
# two = "hcsFMMfFFhFp"
# list1 = []
# list2 = []

# match = []

# for char in one:
#     list1.append(char)

# for char in two:
#     list2.append(char)

# for element in list1:
#     if element in list2:
#         match.append(element)

# print(match)

# string = "vJrwpWtwJgWrhcsFMMfFFhFp"
# x = len(string)
# half1 = slice(0, x//2)
# half2 = slice(x//2, x)

# print(string[half1])
# print(string[half2])

rucksack = []
compartment1 = []
compartment2 = []
match = []

with open("rucksacks.txt") as f:
    for each in f:
        rucksack.append(each.strip())

# split each string from list in half.

for letter in rucksack:
    L = len(rucksack)
    half1 = slice(0, L//2)
    half2 = slice(L//2, L)


# iterate both new lists to make another list with matching elements.

# convert matching elements to their values.

# total values.