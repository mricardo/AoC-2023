import re
with open("Day1/Day1_input.txt", "r") as file:
    lines = file.readlines()

calibration = 0
for line in lines:
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line.strip())
    dict = {'one': '1', 'two': '2', 'three': '3',
             'four': '4', 'five': '5', 'six': '6',
             'seven': '7', 'eight': '8', 'nine': '9'}

    n1 = numbers[0] if numbers[0].isdigit() else dict[numbers[0]]
    n2 = numbers[-1] if numbers[-1].isdigit() else dict[numbers[-1]]

    calibration += int(f"{n1}{n2}")

print(calibration)