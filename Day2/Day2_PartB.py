import re

with open("Day2/Day2_input.txt", "r") as file:
    lines = file.readlines()

total_power = 0
for line in lines:
    l = line.strip()

    game = int(l[5 : l.index(":")].strip())

    blue = [int(e) for e in re.findall(r'(\d+) blue', l)]
    red = [int(e) for e in re.findall(r'(\d+) red', l)]
    green = [int(e) for e in re.findall(r'(\d+) green', l)]

    max_blue = max(blue) 
    max_red = max(red) 
    max_green = max(green)

    total_power += max_blue * max_red * max_green

print(total_power)