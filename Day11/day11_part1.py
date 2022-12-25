# file = open("day11_sample_input.txt")
file = open("day11_input.txt")

# NUMBER_OF_MONKEYS = 4
NUMBER_OF_MONKEYS = 8
ROUNDS = 20
current_round = 1
current_monkey = 0
monkey_items = []
monkey_op = []
monkey_test = []
monkey_destination = []
inspection_count = []

for i in range(NUMBER_OF_MONKEYS):
    monkey_items.append([])
    monkey_op.append([])
    monkey_test.append(0)
    monkey_destination.append([])
    inspection_count.append(0)


def add_operation(line_text):
    operation = ""
    output_list = []
    equation = line_text.split("=")[1].strip()
    if "+" in equation:
        operation = "+"
    elif "*" in equation:
        operation = "*"
    output_list.append(operation)
    try:
        number_1 = int(equation.split(operation)[0].strip())
    except ValueError:
        number_1 = equation.split(operation)[0].strip()
    output_list.append(number_1)
    try:
        number_2 = int(equation.split(operation)[1].strip())
    except ValueError:
        number_2 = equation.split(operation)[1].strip()
    output_list.append(number_2)
    return output_list


for line in file:
    line = line.strip()
    if line.startswith("Monkey"):
        current_monkey = int(line.split()[1].split(":")[0])
    elif line.startswith("Starting"):
        numbers = line.split(":")[1].strip()
        list_numbers = numbers.split(",")
        for number in list_numbers:
            monkey_items[current_monkey].append(int(number))
    elif line.startswith("Operation"):
        monkey_op[current_monkey] = add_operation(line)
    elif line.startswith("Test"):
        test_number = int(line.split("by")[1].strip())
        monkey_test[current_monkey] = test_number
    elif line.startswith("If true"):
        destination_1 = int(line.split("monkey")[1].strip())
        monkey_destination[current_monkey].append(destination_1)
    elif line.startswith("If false"):
        destination_2 = int(line.split("monkey")[1].strip())
        monkey_destination[current_monkey].append(destination_2)

while True:
    for monkey in monkey_items:
        current_monkey = monkey_items.index(monkey)
        for item in monkey:
            worry_level = item
            # add to inspection count
            inspection_count[current_monkey] += 1
            # calculate new worry level
            if monkey_op[current_monkey][1] == "old":
                x = worry_level
            else:
                x = monkey_op[current_monkey][1]
            if monkey_op[current_monkey][2] == "old":
                y = worry_level
            else:
                y = monkey_op[current_monkey][2]
            if monkey_op[current_monkey][0] == "+":
                worry_level = x + y
            else:
                worry_level = x * y
            # divide worry level by 3
            worry_level = worry_level//3
            # test case
            if worry_level % monkey_test[current_monkey] == 0:
                new_monkey = monkey_destination[current_monkey][0]
            else:
                new_monkey = monkey_destination[current_monkey][1]
            monkey_items[new_monkey].append(worry_level)
        monkey_items[current_monkey] = []
    current_round += 1
    if current_round > ROUNDS:
        break

first_highest = max(inspection_count)
inspection_count.remove(max(inspection_count))
second_highest = max(inspection_count)
part1_answer = first_highest * second_highest
print(part1_answer)
