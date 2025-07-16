import re
import math
from numpy import multiply
from collections import defaultdict
 
 # right, down, left, up, down-right, up-left, up-right, down-left
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def gear(lines, row_idx, col_idx):
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    for dr, dc in DIRECTIONS:
        nr, nc = row_idx + dr, col_idx + dc

        if 0 <= nr <= max_row and 0 <= nc <= max_col and lines[nr][nc] == '*':
            return (nr, nc)

    return None

with open("Day3/Day3_input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]

gears = defaultdict(list)

for row_idx, line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        number = int(match.group(0))
        start_col, end_col = match.span()
        
        is_part_number = False

        for col_idx in range(start_col, end_col):
            gear_pos = gear(lines, row_idx, col_idx)
            if gear_pos:
                gears[gear_pos].append(number)
                break

total_gear_ratio = 0
for g in gears.values():
    if len(g) == 2:
        total_gear_ratio += math.prod(g)
        
print(f"Total Gear Ratio: {total_gear_ratio}")