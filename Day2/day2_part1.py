file = open("day2_input.txt")

game_choices = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
score = 0

for line in file:
    value = line.strip()
    opponent_choice = value.split()[0]
    my_choice = value.split()[1]
    draw = False
    win = False
    lose = False
    if game_choices[opponent_choice] == game_choices[my_choice]:
        draw = True
    elif (game_choices[opponent_choice] == "Rock" and game_choices[my_choice] == "Paper") or (
            game_choices[opponent_choice] == "Paper" and game_choices[my_choice] == "Scissors") or (
            game_choices[opponent_choice] == "Scissors" and game_choices[my_choice] == "Rock"):
        win = True
    else:
        lose = True
    if draw:
        score += 3
    if win:
        score += 6
    if game_choices[my_choice] == "Rock":
        score += 1
    if game_choices[my_choice] == "Paper":
        score += 2
    if game_choices[my_choice] == "Scissors":
        score += 3
print(score)
