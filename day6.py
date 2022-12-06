dataStreamArray = []

with open("day6.txt") as dataStream:
    for data in dataStream:
        for letter in data:
            dataStreamArray.append(letter)

print(dataStreamArray)