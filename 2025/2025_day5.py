# Read and parse the input file
with open('2025/day5_real.txt', 'r') as f:
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

print("Rules:", rules)
print("Updates:", updates)

def check_if_is_in_rules(i, rules):

    for rule in rules:
        if rule[0] <= i <= rule[1]:
            # print(f"{i} is valid under rule {rule}")
            return True
    # print(f"{i} is NOT valid under any rule")
    return False


good_ingredient_count = 0
for i in updates:
    is_good = check_if_is_in_rules(i, rules)
    if is_good:
        print(f"ingredient {i} is good to go!") 
        good_ingredient_count += 1

print(f"Total good ingredients: {good_ingredient_count}")