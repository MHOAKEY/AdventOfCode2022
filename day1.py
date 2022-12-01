arrayOfCals = []

with open('elfCalories.txt') as f:
    for line in f:
        arrayOfCals.append(line.strip())

print(arrayOfCals)




