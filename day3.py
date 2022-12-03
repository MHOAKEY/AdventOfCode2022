rucksack = []
splitRuckSack = []
match = []
values = []

with open("rucksacks.txt") as txt:
    for each in txt:
        rucksack.append(each.strip())


for string in rucksack:
    middle = int(len(string) / 2)
    half1 = string[0:middle]
    half2 = string[middle:]
    splitRuckSack.append([half1, half2])
    

for eachArray in splitRuckSack:
    for letter in eachArray[0]:
        if eachArray[1].find(letter) != -1:
            match.append(letter)
            break


lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for letter in match:
    for lowerletter in lower:
        if letter == lowerletter:
            values.append(lower.index(lowerletter) + 1)
    for upperletter in upper:
        if letter == upperletter:
            values.append(upper.index(upperletter) + 27)


valuesSum = 0

for num in values:
    valuesSum += num

print(valuesSum)

