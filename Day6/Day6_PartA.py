import re

def calculate_records(time, distance):
   total_records = 0
   for i in range(time):
      distance_traveled = (time - i) * i
      if distance_traveled > distance:
         total_records += 1

   return total_records

with open("Day6/Day6_input.txt") as file:
    lines = file.readlines()

time = [int(e) for e in re.findall(r'\d+', lines[0])]
distance = [int(e) for e in re.findall(r'\d+', lines[1])]

total_records = 0
for i in range(len(time)):
   records = calculate_records(time[i], distance[i])
   total_records = records if total_records == 0 else total_records * records

print (f"Total records: {total_records}")