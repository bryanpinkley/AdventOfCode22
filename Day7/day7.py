# file = open("day7_sample_input.txt")
file = open("day7_input.txt")

dir_dict = {"/": {}}

# Read each line of input file
for line in file:
    line_cleaned = line.strip()
    # change current_dir to outmost directory
    if line_cleaned.startswith("$ cd /"):
        current_dir = "/"
    # change current_dir to one directory out
    elif line_cleaned.startswith("$ cd .."):
        up_current_dir = current_dir.split("/")[0:-2]
        up_current_dir = [i for i in up_current_dir if i]
        if not up_current_dir:
            current_dir = "/"
        else:
            current_dir = "/"
            for dirs in up_current_dir:
                current_dir = current_dir + dirs + "/"
    # change current_dir to specified directory
    # add this directory to dir_dict if it doesn't exist
    elif line_cleaned.startswith("$ cd"):
        new_dir = line_cleaned.split("cd")[1].strip()
        current_dir = current_dir + new_dir + "/"
        if current_dir not in dir_dict:
            dir_dict[current_dir] = {}
    # don't do anything if the command is list. We will read the data on the following lines next
    elif line_cleaned.startswith("$ ls"):
        pass
    # read the data. Don't care about the directories. Only record the file names and their sizes
    else:
        if line_cleaned[0].isdigit():
            file_size = int(line_cleaned.split()[0])
            file_name = line_cleaned.split()[1]
            dir_dict[current_dir][file_name] = file_size

# store total sizes in each directory. This is only the sizes of the files in that directory, and not subdirectories
sizes = {}
for keys in dir_dict:
    temp_dict = dir_dict[keys]
    total_size = sum(temp_dict.values())
    sizes[keys] = total_size

# now we store the sizes of all the files in the directory and all subdirectories
total_sizes = {}
for keys in sizes:
    if keys not in total_sizes:
        total_sizes[keys] = 0
    for sub_keys in sizes:
        if keys == sub_keys:
            total_sizes[keys] += sizes[keys]
        elif sub_keys.startswith(keys):
            total_sizes[keys] += sizes[sub_keys]

# sum all the directories who's total size is less than or equal to 100000
part_1_answer = 0
for keys in total_sizes:
    if total_sizes[keys] <= 100000:
        part_1_answer += total_sizes[keys]

print(part_1_answer)

total_unused_space = 70000000 - total_sizes["/"]
deletion_required = 30000000 - total_unused_space
minimum_deletion = 0
for keys in total_sizes:
    if total_sizes[keys] >= deletion_required:
        if minimum_deletion == 0:
            minimum_deletion = total_sizes[keys]
        elif total_sizes[keys] < minimum_deletion:
            minimum_deletion = total_sizes[keys]
part_2_answer = minimum_deletion
print(part_2_answer)
