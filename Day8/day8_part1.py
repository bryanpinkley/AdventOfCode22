# file = open("day8_sample_input.txt")
file = open("day8_input.txt")

all_trees_list = []

for line in file:
    sub_tree_array = []
    line_cleaned = line.strip()
    for number in line_cleaned:
        sub_tree_array.append(number)
    all_trees_list.append(sub_tree_array)

visible_tree_counter = 0
vertical_index = 0

for line in all_trees_list:
    if vertical_index == 0 or vertical_index == len(all_trees_list) - 1:
        visible_tree_counter += len(line)
    else:
        horizontal_index = 0
        for number in line:
            if horizontal_index == 0 or horizontal_index == len(line) - 1:
                visible_tree_counter += 1
            else:
                max_tree_height_top = 0
                max_tree_height_bottom = 0
                max_tree_height_right = 0
                max_tree_height_left = 0
                for i in range(0, vertical_index):
                    tree_height_top = int(all_trees_list[i][horizontal_index])
                    if tree_height_top > max_tree_height_top:
                        max_tree_height_top = tree_height_top
                for i in range(vertical_index+1, len(all_trees_list)):
                    tree_height_bottom = int(all_trees_list[i][horizontal_index])
                    if tree_height_bottom > max_tree_height_bottom:
                        max_tree_height_bottom = tree_height_bottom
                for i in range(0, horizontal_index):
                    tree_height_left = int(line[i])
                    if tree_height_left > max_tree_height_left:
                        max_tree_height_left = tree_height_left
                for i in range(horizontal_index+1, len(line)):
                    tree_height_right = int(line[i])
                    if tree_height_right > max_tree_height_right:
                        max_tree_height_right = tree_height_right
                if max_tree_height_top < int(number) or max_tree_height_bottom < int(number) or max_tree_height_left < int(number) or max_tree_height_right < int(number):
                    visible_tree_counter += 1
            horizontal_index += 1
    vertical_index += 1

print(visible_tree_counter)
