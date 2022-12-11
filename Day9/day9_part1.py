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
t_position = [0, 0]
tail_tracker = []

for line in file:
    line = line.strip()
    direction = line.split()[0]
    moves = int(line.split()[1])
    for i in range(1, moves+1):
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
        # If they are on the same spot, do nothing
        if h_position == t_position:
            pass
        # If the tail is touching the head, do nothing
        elif (h_position[0]-1 <= t_position[0] <= h_position[0]+1) and (h_position[1]-1 <= t_position[1] <= h_position[1]+1):
            pass
        # Need to move the tail
        else:
            t_position = move_tail(h_position, t_position)

        if t_position not in tail_tracker:
            tail_tracker.append([t_position[0], t_position[1]])
print(len(tail_tracker))
