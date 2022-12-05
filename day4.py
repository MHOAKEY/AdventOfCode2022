array = []
array2 = []

with open('day4.txt') as campSections:
    for eachSection in campSections:
        array.append(eachSection.strip().split(","))

print(array)



# compare each nested array for over lap