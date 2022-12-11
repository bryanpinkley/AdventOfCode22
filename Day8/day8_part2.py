# file = open("day8_sample_input.txt")
file = open("day8_input.txt")

all_trees_list = []

for line in file:
    sub_tree_array = []
    line_cleaned = line.strip()
    for number in line_cleaned:
        sub_tree_array.append(number)
    all_trees_list.append(sub_tree_array)

vertical_index = 0
max_scenic_score = 0

for line in all_trees_list:
    if vertical_index == 0 or vertical_index == len(all_trees_list) - 1:
        pass
    else:
        horizontal_index = 0
        for number in line:
            number = int(number)
            if horizontal_index == 0 or horizontal_index == len(line) - 1:
                pass
            else:
                scenic_score = 0
                scenic_score_top, scenic_score_bottom, scenic_score_left, scenic_score_right = 0, 0, 0, 0
                top_tree_score = 0
                bottom_tree_score = 0
                left_tree_score = 0
                right_tree_score = 0
                for i in range(vertical_index - 1, -1, -1):
                    scenic_score_top += 1
                    tree_height_top = int(all_trees_list[i][horizontal_index])
                    if tree_height_top >= number:
                        break
                for i in range(vertical_index + 1, len(all_trees_list)):
                    scenic_score_bottom += 1
                    tree_height_bottom = int(all_trees_list[i][horizontal_index])
                    if tree_height_bottom >= number:
                        break
                for i in range(horizontal_index - 1, -1, -1):
                    scenic_score_left += 1
                    tree_height_left = int(line[i])
                    if tree_height_left >= number:
                        break
                for i in range(horizontal_index + 1, len(line)):
                    scenic_score_right += 1
                    tree_height_right = int(line[i])
                    if tree_height_right >= number:
                        break
                total_scenic_score = scenic_score_top * scenic_score_bottom * scenic_score_left * scenic_score_right
                if total_scenic_score > max_scenic_score:
                    max_scenic_score = total_scenic_score
            horizontal_index += 1
    vertical_index += 1

print(max_scenic_score)
