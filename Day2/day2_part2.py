file = open("day2_input.txt")

game_choices = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
score = 0

for line in file:
    value = line.strip()
    opponent_choice = value.split()[0]
    required_result = value.split()[1]
    draw = False
    win = False
    lose = False
    my_choice = ""
    if required_result == "X":
        lose = True
    elif required_result == "Y":
        draw = True
    else:
        win = True

    if draw:
        my_choice = game_choices[opponent_choice]
    if win:
        if game_choices[opponent_choice] == "Rock":
            my_choice = "Paper"
        elif game_choices[opponent_choice] == "Paper":
            my_choice = "Scissors"
        else:
            my_choice = "Rock"
    if lose:
        if game_choices[opponent_choice] == "Rock":
            my_choice = "Scissors"
        elif game_choices[opponent_choice] == "Paper":
            my_choice = "Rock"
        else:
            my_choice = "Paper"
    if draw:
        score += 3
    if win:
        score += 6
    if my_choice == "Rock":
        score += 1
    if my_choice == "Paper":
        score += 2
    if my_choice == "Scissors":
        score += 3
print(score)
