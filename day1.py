arrayOfCals = []

with open('elfCalories.txt') as f:
    for eachLine in f:
        arrayOfCals.append(eachLine.strip())
        

for index in range(0, len(arrayOfCals)):
    if arrayOfCals[index] != "":
        arrayOfCals[index] = int(arrayOfCals[index])


eachElfCalTotalArray = []
x = 0

for num in arrayOfCals:
    if num != "":
        x += num
    else: 
        eachElfCalTotalArray.append(x)
        x = 0


mostCals = eachElfCalTotalArray[0]


for i in range(0, len(eachElfCalTotalArray)):
    if (eachElfCalTotalArray[i] > mostCals):
        mostCals = eachElfCalTotalArray[i]


eachElfCalTotalArray.sort()
totalOfThree = 0

for i in eachElfCalTotalArray[-3:]:
    totalOfThree += i


print(totalOfThree)
