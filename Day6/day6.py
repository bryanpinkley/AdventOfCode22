from collections import Counter

file = open("day6_input.txt")
counter = 0

for line in file:
    while counter < len(line):
        marker = line[counter] + line[counter+1] + line[counter+2] + line[counter+3]
        freq = Counter(marker)
        if len(freq) == 4:
            print(counter+4)
            break
        counter += 1

    counter = 0
    while counter < len(line):
        marker = ""
        for i in range(14):
            marker += line[counter+i]
        freq = Counter(marker)
        if len(freq) == 14:
            print(counter+14)
            break
        counter += 1
