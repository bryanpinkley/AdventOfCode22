file = open("day4_input.txt")

overlap_list_1 = []
overlap_list_2 = []

for line in file:
    value = line.strip()
    first_value = value.split(",")[0]
    second_value = value.split(",")[1]
    first_value_bottom = int(first_value.split("-")[0])
    first_value_top = int(first_value.split("-")[1])
    second_value_bottom = int(second_value.split("-")[0])
    second_value_top = int(second_value.split("-")[1])
    if (first_value_top >= second_value_top and first_value_bottom <= second_value_bottom) or (
            first_value_top <= second_value_top and first_value_bottom >= second_value_bottom):
        overlap_list_1.append(value)
    if (first_value_top <= second_value_top and first_value_top >= second_value_bottom) or (
            second_value_top <= first_value_top and second_value_top >= first_value_bottom) or (
            first_value_bottom >= second_value_bottom and first_value_bottom <= second_value_top) or (
            second_value_bottom >= first_value_bottom and second_value_bottom <= first_value_top):
        overlap_list_2.append(value)

print(len(overlap_list_1))
print(len(overlap_list_2))
