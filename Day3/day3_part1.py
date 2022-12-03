file = open("day3_input.txt")

priority = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", 'y', "z", "A", "B", "C", 'D', "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", 'U', "V", "W", "X", "Y", "Z"]
score = 0

for line in file:
    value = line.strip()
    first_half = value[:len(value) // 2]
    second_half = value[len(value) // 2:]
    for character in first_half:
        if character in second_half:
            score += priority.index(character) + 1
            break

print(score)
