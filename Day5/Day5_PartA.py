import re

def list_of_digits(s):
    return list(map(int, re.findall(r'(\d+)', s)))

def apply_mapping(start_idx, end_idx):
    mapping = []
    for line in lines[start_idx + 1: end_idx-1]:
        destination, source, length = list_of_digits(line)
 
        mapping.append((destination, source, length))
    
    return mapping

def get_location(search_token, map_idx, maps_list):
    if map_idx >= len(maps_list):
        return search_token

    current_map = maps_list[map_idx]
    
    next_token = -1
    for destination, source, length in current_map:
        if search_token >= source and search_token < source + length:
            idx = search_token - source
            next_token = destination + idx
    
    if next_token == -1:
        next_token = search_token    

    return get_location(next_token, map_idx + 1, maps_list)

with open("Day5_input.txt", "r") as file:
    lines = file.read().splitlines()

initial_seeds = list_of_digits(lines[0])

seed_to_soil_idx = lines.index('seed-to-soil map:')
soil_to_fertilizer_idx = lines.index('soil-to-fertilizer map:')
fertilizer_to_water_idx = lines.index('fertilizer-to-water map:')
water_to_light_idx = lines.index('water-to-light map:')
light_to_temperature_idx = lines.index('light-to-temperature map:')
temperature_to_humidity_idx = lines.index('temperature-to-humidity map:')
humidity_to_location_idx = lines.index('humidity-to-location map:')

seed_to_soil_map = apply_mapping(seed_to_soil_idx, soil_to_fertilizer_idx)
soil_to_fertilizer_map = apply_mapping(soil_to_fertilizer_idx, fertilizer_to_water_idx)
fertilizer_to_water_map = apply_mapping(fertilizer_to_water_idx, water_to_light_idx)
water_to_light_map = apply_mapping(water_to_light_idx, light_to_temperature_idx)
light_to_temperature_map = apply_mapping(light_to_temperature_idx, temperature_to_humidity_idx)
temperature_to_humidity_map = apply_mapping(temperature_to_humidity_idx, humidity_to_location_idx)   
humidity_to_location_map = apply_mapping(humidity_to_location_idx, len(lines)+1)

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
for seed in initial_seeds:
    location = get_location(seed, 0, maps_list)
    
    if location < lowest_location:
        lowest_location = location

print("Lowest location:", lowest_location)
