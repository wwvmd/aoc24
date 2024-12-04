with open('day4/input/test.txt', 'r') as file:
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

for xpos in x_positions:
    #for each xpos check if there is M adjacent to it
        


def find_character_m(rows):
    positions = []
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char == 'M':
                positions.append((i, j))
    return positions

m_positions = find_character_m(rows)
print(m_positions)


for xpos in x_positions:
    #for each xpos check if there is M adjacent to it
    # check right
    if (xpos[0], xpos[1] + 1) in m_positions:
        print('X and M are adjacent')
        
    #         