file = open("day3_input.txt")

priority = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", 'y', "z", "A", "B", "C", 'D', "E", "F", "G", "H", 'I', "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", 'U', "V", "W", "X", "Y", "Z"]
score = 0
group = []
counter = 0


def find_match(first, second, third):
    for character in first:
        if character in second and character in third:
            score = priority.index(character) + 1
            break
    return score


for line in file:
    counter += 1
    if len(group) == 3:
        score += find_match(group[0], group[1], group[2])
        group = []
    group.append(line.strip())
    if counter == 300:
        score += find_match(group[0], group[1], group[2])
print(score)
