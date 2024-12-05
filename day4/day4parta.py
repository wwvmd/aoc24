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




xmasCount = 0
for xpos in x_positions:
    #for each xpos check if there is M adjacent to it
    # check right
    if (xpos[0], xpos[1] + 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0], xpos[1] + 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0], xpos[1] + 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check left    
    if (xpos[0], xpos[1] - 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0], xpos[1] - 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0], xpos[1] - 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check up
    if (xpos[0] - 1, xpos[1]) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] - 2, xpos[1]) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] - 3, xpos[1]) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check down
    if (xpos[0] + 1, xpos[1]) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] + 2, xpos[1]) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] + 3, xpos[1]) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check up right
    if (xpos[0] - 1, xpos[1] + 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] - 2, xpos[1] + 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] - 3, xpos[1] + 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check up left
    if (xpos[0] - 1, xpos[1] - 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] - 2, xpos[1] - 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] - 3, xpos[1] - 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check down right
    if (xpos[0] + 1, xpos[1] + 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] + 2, xpos[1] + 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] + 3, xpos[1] + 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
    # check down left
    if (xpos[0] + 1, xpos[1] - 1) in m_positions:
        print('X and M are adjacent')
        if (xpos[0] + 2, xpos[1] - 2) in a_positions:
            print('M and A are adjacent')
            if (xpos[0] + 3, xpos[1] - 3) in s_positions:
                print('A and S are adjacent')
                xmasCount += 1
print(xmasCount)