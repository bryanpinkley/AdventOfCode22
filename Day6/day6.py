from collections import Counter

file = open("day6_input.txt")
counter = 0

for line in file:
    while counter < len(line):
        marker = line[counter] + line[counter+1] + line[counter+2] + line[counter+3]
        freq = Counter(marker)
        if len(freq) == 4:
            print(marker)
            print(counter+4)
            break
        counter += 1

