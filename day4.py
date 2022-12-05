arrays = []
array2 = []
array3 = []

with open('day4.txt') as campSections:
    for eachSection in campSections:
        arrays.append(eachSection.strip().split(","))

for eachArray in arrays:
    x = eachArray[0].split("-")
    y = eachArray[1].split("-")
    array2.append([x,y])

for eachSection in array2:
    elf1Start = eachSection[0][0]
    elf1End = eachSection[0][1]
    elf2Start = eachSection[1][0]
    elf2End = eachSection[1][1]
