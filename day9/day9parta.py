with open('day9/input/real.txt', 'r') as file:
    data = file.read()

print(data)

s = []

blank = False
id = 0
for c in data:
    print(c)
    number = int(c)
    
    for i in range(int(c)):
        if blank:
            s.append('.')
        else:
            s.append(id)
    if not blank:
        id += 1
    blank = not blank

print(s)    


dot_count = s.count('.')
print(f"Number of elements containing '.': {dot_count}")

for i in range(dot_count):
    c = s.pop()
    if '.' in s:
        index = s.index('.')
        s[index] = c

print(s)

id_counter = 0
cumulative_sum = 0

for element in s:
    cumulative_sum += id_counter * element
    id_counter += 1

print(f"Cumulative sum: {cumulative_sum}")

    


