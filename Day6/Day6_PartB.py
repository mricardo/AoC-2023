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

time = int(''.join(str(t) for t in time))
distance = int(''.join(str(d) for d in distance))
print (f"Time: {time}, Distance: {distance}")

total_records = 0
records = calculate_records(time, distance)
total_records = records if total_records == 0 else total_records * records

print (f"Total records: {total_records}")
