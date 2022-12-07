file = open("day5_input.txt")

crate_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
initial_stage = True
part1_solution = ""

for line in file:
    if initial_stage:
        if line == " 1   2   3   4   5   6   7   8   9\n":
            initial_stage = False
        else:
            counter = 0
            stack = 1
            for character in line:
                if character == "\n":
                    break
                if counter == 1 or (counter-1) % 4 == 0:
                    if character != " ":
                        crate_dict[stack].insert(0, character)
                    stack += 1
                counter += 1
    elif not initial_stage:
        if line == "\n":
            pass
        else:
            move_quantity = int(line.split("move")[1].split("from")[0].strip())
            original_stack = int(line.split("from")[1].split("to")[0].strip())
            new_stack = int(line.split("from")[1].split("to")[1].strip())
            for i in range(1, move_quantity+1):
                letter_to_move = crate_dict[original_stack][-1]
                crate_dict[new_stack].append(letter_to_move)
                crate_dict[original_stack].pop(len(crate_dict[original_stack])-1)

for stack in crate_dict:
    last_item = crate_dict[stack][-1]
    part1_solution += last_item
print(part1_solution)
