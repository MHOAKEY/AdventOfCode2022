terminalArrays = []

with open ("day7.txt") as terminalOutput:
    for line in terminalOutput:
        terminalArrays.append(line.strip("\n"))

print(terminalArrays)