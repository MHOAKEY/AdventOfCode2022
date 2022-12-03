rucksack = []
# splitRuckSack = []
# match = []
# values = []
valuesPart2 = []
totalPart2 = 0


with open("rucksacks.txt") as txt:
    for each in txt:
        rucksack.append(each.strip())

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


for index in range(0, len(rucksack), 3):
        common = (set(rucksack[index]) & set(rucksack[index+1]) & set(rucksack[index+2])).pop()
        for each in common:
            for letter in lower:
                if each == letter:
                    valuesPart2.append(lower.index(letter) + 1)
            for letters in upper:
                if each == letters:
                    valuesPart2.append(upper.index(letters) + 27)

for num in valuesPart2:
    totalPart2 += num

print(totalPart2)


# for string in rucksack:
#     middle = int(len(string) / 2)
#     half1 = string[0:middle]
#     half2 = string[middle:]
#     splitRuckSack.append([half1, half2])
    

# for eachArray in splitRuckSack:
#     for letter in eachArray[0]:
#         if eachArray[1].find(letter) != -1:
#             match.append(letter)
#             break


# lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# for letter in match:
#     for lowerletter in lower:
#         if letter == lowerletter:
#             values.append(lower.index(lowerletter) + 1)
#     for upperletter in upper:
#         if letter == upperletter:
#             values.append(upper.index(upperletter) + 27)


# valuesSum = 0

# for num in values:
#     valuesSum += num

# print(valuesSum)

