shape_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

play_map = {
    ('A', 'X'): 'Scissors',
    ('A', 'Y'): 'Rock',
    ('A', 'Z'): 'Paper',
    ('B', 'X'): 'Rock',
    ('B', 'Y'): 'Paper',
    ('B', 'Z'): 'Scissors',
    ('C', 'X'): 'Paper',
    ('C', 'Y'): 'Scissors',
    ('C', 'Z'): 'Rock'
}

outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

print("Enter your rounds:")

total = 0
while True:
    line = input().strip()
    if line == "":
        break
    try:
        opp, outcome = line.split()
        shape = play_map[(opp, outcome)]
        total += shape_score[shape] + outcome_score[outcome]
    except Exception:
        print("Invalid input, please use format like 'A X'")

print("Total score:", total)
