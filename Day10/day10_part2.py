# file = open("day10_sample_input.txt")
file = open("day10_input.txt")

cycle = 0
sprite_location = 1

crt_line = ""

addx_tracker = False


def render_sprite(cycle, sprite_location) -> str:
    if cycle-1 <= sprite_location <= cycle+1:
        return "#"
    else:
        return "."


for line in file:
    line = line.strip()
    crt_line += render_sprite(cycle, sprite_location)
    if line.startswith("addx"):
        addx_tracker = True
    if cycle != 39:
        cycle += 1
    else:
        cycle = 0
    if addx_tracker:
        crt_line += render_sprite(cycle, sprite_location)
        sprite_location += int(line.split()[1])
        if cycle != 39:
            cycle += 1
        else:
            cycle = 0
        addx_tracker = False


print(crt_line[:len(crt_line)//6])
print(crt_line[len(crt_line)//6:len(crt_line)*2//6])
print(crt_line[len(crt_line)*2//6:len(crt_line)*3//6])
print(crt_line[len(crt_line)*3//6:len(crt_line)*4//6])
print(crt_line[len(crt_line)*4//6:len(crt_line)*5//6])
print(crt_line[len(crt_line)*5//6:])
