import re

with open("Day2/Day2_input.txt", "r") as file:
    lines = file.readlines()

MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14

game_ids = 0
for line in lines:
    l = line.strip()

    game = int(l[5 : l.index(":")].strip())

    blue = [int(e) for e in re.findall(r'(\d+) blue', l)]
    red = [int(e) for e in re.findall(r'(\d+) red', l)]
    green = [int(e) for e in re.findall(r'(\d+) green', l)]

    is_possible = (
        all (e <= MAX_BLUE for e in blue) and
        all (e <= MAX_RED for e in red) and
        all (e <= MAX_GREEN for e in green)
    )
    
    if is_possible:
        game_ids += game

print(game_ids)