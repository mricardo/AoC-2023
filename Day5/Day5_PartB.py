import re

def list_of_digits(s):
    return list(map(int, re.findall(r'(\d+)', s)))

def apply_mapping(start_idx, end_idx, lines):
    mapping = []
    for line in lines[start_idx + 1: end_idx-1]:
        destination, source, length = list_of_digits(line)
 
        mapping.append((destination, source, length))
    
    return mapping

def get_location_by_range(ranges, maps_list, lowest_location, map_idx = 0):    
    if map_idx >= len(maps_list):  
        seed_start, seed_range = ranges.pop(0)
        return seed_start

    mapping = maps_list[map_idx]

    while len(ranges) > 0:        
        seed_start, seed_range = ranges.pop(0)
        
        mapped = False

        for destination_map, source_map, range_map in mapping:            
            
            if seed_start >= source_map and seed_start <= source_map + range_map - 1:
                mapped = True
            
                seed_offset = (seed_start - source_map)
        
                destination_start = destination_map + seed_offset

                range_remaining = min(range_map, seed_range)
                
                location = get_location_by_range([(destination_start, range_remaining)], maps_list, lowest_location, map_idx + 1)

                if location < lowest_location:                    
                    lowest_location = location
                
                if seed_start + seed_range - 1 > source_map + range_map - 1:                    
                    new_destination_start = source_map + range_map
                    new_destination_range = seed_start + seed_range - new_destination_start
                    ranges.insert(0, (new_destination_start, new_destination_range))
                    
        if not mapped:           
           ranges.insert(0, (seed_start, seed_range))           
           location = get_location_by_range(ranges, maps_list, lowest_location, map_idx + 1)

           if location < lowest_location:                             
               lowest_location = location
            
    return lowest_location 

with open("Day5\Day5_input.txt", "r") as file:
    lines = file.read().splitlines()

seeds_range = list_of_digits(lines[0])
seeds_range = [(seeds_range[i], seeds_range[i+1]) for i in range(0, len(seeds_range), 2)]

seed_to_soil_idx = lines.index('seed-to-soil map:')
soil_to_fertilizer_idx = lines.index('soil-to-fertilizer map:')
fertilizer_to_water_idx = lines.index('fertilizer-to-water map:')
water_to_light_idx = lines.index('water-to-light map:')
light_to_temperature_idx = lines.index('light-to-temperature map:')
temperature_to_humidity_idx = lines.index('temperature-to-humidity map:')
humidity_to_location_idx = lines.index('humidity-to-location map:')

seed_to_soil_map = apply_mapping(seed_to_soil_idx, soil_to_fertilizer_idx, lines)
soil_to_fertilizer_map = apply_mapping(soil_to_fertilizer_idx, fertilizer_to_water_idx, lines)
fertilizer_to_water_map = apply_mapping(fertilizer_to_water_idx, water_to_light_idx, lines)
water_to_light_map = apply_mapping(water_to_light_idx, light_to_temperature_idx, lines)
light_to_temperature_map = apply_mapping(light_to_temperature_idx, temperature_to_humidity_idx, lines)
temperature_to_humidity_map = apply_mapping(temperature_to_humidity_idx, humidity_to_location_idx, lines)   
humidity_to_location_map = apply_mapping(humidity_to_location_idx, len(lines)+1, lines)

maps_list = [
    seed_to_soil_map,
    soil_to_fertilizer_map, 
    fertilizer_to_water_map,
    water_to_light_map, 
    light_to_temperature_map, 
    temperature_to_humidity_map,
    humidity_to_location_map
    ]

lowest_location = float('inf')
for r in seeds_range:
    location = get_location_by_range([r], maps_list, float('inf'))
    if location < lowest_location and location> 0:
        lowest_location = location

print("Lowest location:", lowest_location)
