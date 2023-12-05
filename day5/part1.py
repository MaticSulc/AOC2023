from functools import reduce

def apply_mapping_rules(value, mapping): #really cool .. not sure this will work for part 2
    _, *ranges = mapping.split('\n')
    for rule in ranges:
        destination, source, length = map(int, rule.split())
        if source <= value < source + length:
            return value - source + destination
    else:
        return value

with open("sample", 'r') as file:
        input_data = file.read().split('\n\n')

seeds, *maps = input_data

seed_values = list(map(int, seeds.split()[1:])) #get seeds
min_transformed_value = min(
	reduce(apply_mapping_rules, maps, seed_val) for seed_val in seed_values
)

print(min_transformed_value)
