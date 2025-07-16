import re
 
 # right, down, left, up, down-right, up-left, up-right, down-left
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def sweep_special_character(lines, row_idx, col_idx):
    max_row = len(lines) - 1
    max_col = len(lines[0]) - 1

    return any(
        0 <= nr <= max_row and 0 <= nc <= max_col and
        lines[nr][nc] != '.' and not lines[nr][nc].isnumeric()
        for dr, dc in DIRECTIONS
        for nr, nc in [(row_idx + dr, col_idx + dc)]
    )

with open("Day3/Day3_input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]

total_part_number = 0

for row_idx, line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        number_str = match.group(0)
        start_col, end_col = match.span()
        
        is_part_number = False

        for col_idx in range(start_col, end_col):
            if sweep_special_character(lines, row_idx, col_idx):
                is_part_number = True
                break
        
        if is_part_number:
            total_part_number += int(number_str)
   
print(f"Total Part Number: {total_part_number}")
