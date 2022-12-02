file = open("day1_input.txt")

calories_list = []
calories = 0

for line in file:
    value = line.strip()
    if value:
        calories += int(value)
    else:
        calories_list.append(calories)
        calories = 0

part1_answer = max(calories_list)
print(part1_answer)

calories_list_sorted = sorted(calories_list, reverse=True)
part2_answer = calories_list_sorted[0] + calories_list_sorted[1] + calories_list_sorted[2]
print(part2_answer)
