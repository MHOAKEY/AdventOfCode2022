dataStreamArray = []

with open("day6.txt") as dataStream:
    for data in dataStream:
        for letter in data:
            dataStreamArray.append(letter)

def startOfPacketMarker(data):
    for index in range(len(data)):
        fourLetterCheck = data[index:index + 4]
        if len(set(fourLetterCheck)) == 4:
            return index + 4

print(startOfPacketMarker(dataStreamArray))


def startOfPacketMarkerPart2(data):
    for index in range(len(data)):
        fourLetterCheck = data[index:index + 14]
        if len(set(fourLetterCheck)) == 14:
            return index + 14

print(startOfPacketMarkerPart2(dataStreamArray))
