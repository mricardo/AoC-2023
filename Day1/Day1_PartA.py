import re
with open("Day1/Day1_input.txt", "r") as file:
    lines = file.readlines()

calibration = 0
for line in lines:
    numbers = re.findall(r'\d', line.strip())
    calibration += int(f"{numbers[0]}{numbers[-1]}")

print(calibration)
