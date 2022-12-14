# file = open("day10_sample_input.txt")
file = open("day10_input.txt")

cycle = 1
x = 1
signal_strength = 0
check_20, check_60, check_100, check_140, check_180, check_220 = False, False, False, False, False, False

for line in file:
    line = line.strip()
    if line.startswith("addx"):
        cycle += 2
    elif line.startswith("noop"):
        cycle += 1
        print(f"line: {line}, cycle: {cycle}")
    if cycle == 21 and not check_20:
        signal_strength += 20*x
        print(f"signal strength: {20*x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 61 and not check_60:
        signal_strength += 60*x
        print(f"signal strength: {60 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 101 and not check_100:
        signal_strength += 100*x
        print(f"signal strength: {100 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 141 and not check_140:
        signal_strength += 140*x
        print(f"signal strength: {140 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 181 and not check_180:
        signal_strength += 180*x
        print(f"signal strength: {180 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 221 and not check_220:
        signal_strength += 220*x
        print(f"signal strength: {220 * x}, total: {signal_strength}, cycle: {cycle}")
    if line.startswith("addx"):
        x += int(line.split()[1])
        print(f"line: {line}, cycle: {cycle}, x: {x}")
    if cycle == 20:
        signal_strength += 20*x
        check_20 = True
        print(f"signal strength: {20*x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 60:
        signal_strength += 60*x
        check_60 = True
        print(f"signal strength: {60 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 100:
        signal_strength += 100*x
        check_100 = True
        print(f"signal strength: {100 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 140:
        signal_strength += 140*x
        check_140 = True
        print(f"signal strength: {140 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 180:
        signal_strength += 180*x
        check_180 = True
        print(f"signal strength: {180 * x}, total: {signal_strength}, cycle: {cycle}")
    elif cycle == 220:
        signal_strength += 220*x
        check_220 = True
        print(f"signal strength: {220 * x}, total: {signal_strength}, cycle: {cycle}")
print(signal_strength)
