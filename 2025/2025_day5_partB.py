# Read and parse the input file
with open('2025/day5_sample.txt', 'r') as f:
    content = f.read()

# Split by double newline to separate sections
sections = content.split('\n\n')

# Parse first section: tuples of two integers separated by '-'
rules = []
for line in sections[0].strip().split('\n'):
    if line:
        parts = line.split('-')
        rules.append((int(parts[0]), int(parts[1])))

# Parse second section: list of lines
updates = []
for line in sections[1].strip().split('\n'):
    if line:
        updates.append(int(line))

# print("Rules:", rules)
# print("Updates:", updates)




def merge_ranges(rules):
    """Merge overlapping ranges to avoid double counting"""
    if not rules:
        return []
    
    # Sort rules by start position
    sorted_rules = sorted(rules, key=lambda x: x[0])
    
    merged = [sorted_rules[0]]
    
    for current in sorted_rules[1:]:
        last = merged[-1]
        
        # Check if current range overlaps with last merged range
        if current[0] <= last[1] + 1:
            # Merge: extend the end if current goes further
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            # No overlap, add as new range
            merged.append(current)
    
    return merged

def count_valid_ingredients(rules):
    """Count total valid ingredients after merging overlapping ranges"""
    merged = merge_ranges(rules)
    total = 0
    for rule in merged:
        total += (rule[1] - rule[0] + 1)
    return total

total_valid = count_valid_ingredients(rules)

print(f"Total good ingredients: {total_valid}")