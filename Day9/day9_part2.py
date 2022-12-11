# file = open("day9_sample_input.txt")
file = open("day9_input.txt")


def move_tail(head_position: list, tail_position: list):
    # if row is the same
    if head_position[0] == tail_position[0]:
        if head_position[1] > tail_position[1]:
            tail_position[1] += 1
        else:
            tail_position[1] -= 1
    # if column is the same
    elif head_position[1] == tail_position[1]:
        if head_position[0] > tail_position[0]:
            tail_position[0] += 1
        else:
            tail_position[0] -= 1
    # if diagonal move
    elif head_position[0] > tail_position[0]:
        if head_position[1] > tail_position[1]:
            tail_position[0] += 1
            tail_position[1] += 1
        else:
            tail_position[0] += 1
            tail_position[1] -= 1
    elif head_position[0] < tail_position[0]:
        if head_position[1] > tail_position[1]:
            tail_position[0] -= 1
            tail_position[1] += 1
        else:
            tail_position[0] -= 1
            tail_position[1] -= 1
    return tail_position


# row, column. 0,0 is origin
h_position = [0, 0]
t1_position = [0, 0]
t2_position = [0, 0]
t3_position = [0, 0]
t4_position = [0, 0]
t5_position = [0, 0]
t6_position = [0, 0]
t7_position = [0, 0]
t8_position = [0, 0]
t9_position = [0, 0]
tail_list = [t1_position, t2_position, t3_position, t4_position, t5_position, t6_position, t7_position, t8_position,
             t9_position]

tail_tracker = []

for line in file:
    line = line.strip()
    direction = line.split()[0]
    moves = int(line.split()[1])
    for i in range(1, moves + 1):
        # move head first
        if direction == "R":
            h_position[1] += 1
        elif direction == "L":
            h_position[1] += -1
        elif direction == "U":
            h_position[0] += 1
        elif direction == "D":
            h_position[0] += -1
        # Check where tail is
        tail_counter = 0
        for tail in tail_list:
            tail_position = tail
            if tail_counter == 0:
                front_position = h_position
            else:
                front_position = tail_list[tail_counter - 1]
            # If they are on the same spot, do nothing
            if front_position == tail_position:
                pass
            # If the tail is touching the head, do nothing
            elif (front_position[0] - 1 <= tail_position[0] <= front_position[0] + 1) and (
                    front_position[1] - 1 <= tail_position[1] <= front_position[1] + 1):
                pass
            # Need to move the tail
            else:
                tail_position = move_tail(front_position, tail_position)
            if tail_counter == 8 and tail_position not in tail_tracker:
                tail_tracker.append([tail_position[0], tail_position[1]])
            tail_counter += 1
print(len(tail_tracker))
