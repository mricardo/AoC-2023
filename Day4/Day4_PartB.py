import re
from collections import defaultdict

with open("Day4_test.txt") as file:
    lines = file.read().splitlines()

# initialize a cache to store the number of ways to win for each card
memo = defaultdict(int)
for i in range(len(lines)):
    memo[i] = 1

for card_number, line in enumerate(lines):
    parts = line.split("|")
    winning = {int(n) for n in re.findall(r'\d+', parts[0])[1:]}
    drawn = {int(n) for n in re.findall(r'\d+', parts[1])}
    
    matches = len(winning & drawn)

    for i in range(matches):
        next_card = card_number + i + 1
        memo[next_card] += memo[card_number]

total_score = sum(memo.values())
print(f"Total Score: {total_score}")