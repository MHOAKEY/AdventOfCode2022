terminalArray = []

with open ("day7.txt") as terminalOutput:
    for line in terminalOutput:
        terminalArray.append(line.split("/n"))

print(terminalArray)