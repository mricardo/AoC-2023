import re
import math

with open("Day4/Day4_test.txt", "r") as file:
    lines = file.read().splitlines()

total_score = 0

for line in lines:
    parts = line.split("|")

    winning_numbers = set(re.findall(r'(\d+)', parts[0])[1:])
    drawn_numbers = set(re.findall(r'(\d+)', parts[1]))

    match_numbers = len(winning_numbers & drawn_numbers)
    total_score += int(math.pow(2, match_numbers-1))

print(f"Total Score: {total_score}")