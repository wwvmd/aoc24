with open('day4/input/real.txt', 'r') as file:
    data = file.read()

rows = [list(line) for line in data.splitlines()]
print(rows)

def find_character_x(rows):
    positions = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == 'X':
                positions.append((i, j))
    return positions

x_positions = find_character_x(rows)
print(x_positions)




def find_character_m(rows):
    positions = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == 'M':
                positions.append((i, j))
    return positions

m_positions = find_character_m(rows)
print(m_positions)

def find_character_a(rows):
    positions = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == 'A':
                positions.append((i, j))
    return positions

a_positions = find_character_a(rows)

def find_character_s(rows):
    positions = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == 'S':
                positions.append((i, j))
    return positions

s_positions = find_character_s(rows)




x_masCount = 0
for apos in a_positions:
    #check up left for a M and down right for a S
    possible_x_mas = False
    if (apos[0] - 1, apos[1] - 1) in m_positions and (apos[0] + 1, apos[1] + 1) in s_positions:
        possible_x_mas = True
    elif (apos[0] - 1, apos[1] - 1) in s_positions and (apos[0] + 1, apos[1] + 1) in m_positions:
        possible_x_mas = True
    if possible_x_mas:
        #check up right for an M and down left for an S
        if (apos[0] - 1, apos[1] + 1) in m_positions and (apos[0] + 1, apos[1] - 1) in s_positions:
            print(f"X-MAS found at {apos}")
            x_masCount += 1
        elif (apos[0] - 1, apos[1] + 1) in s_positions and (apos[0] + 1, apos[1] - 1) in m_positions:
            print(f"X-MAS found at {apos}")
            x_masCount += 1
print(x_masCount)









print(x_masCount)