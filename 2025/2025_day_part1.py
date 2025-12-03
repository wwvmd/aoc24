import random

# Array of integers between 0 and 99
dial = list(range(100))
# print(dial)


arrow_pointer = 50
arrow_pointer = dial[50]

print("Arrow Pointer Index:", arrow_pointer)

def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    instructions_list = []

    for line in lines:
        line.strip()
        instruction = line[0],int(line[1:])
        # print(f'turn direction {instruction[0]} number of notches {instruction[1]}')
        instructions_list.append(instruction)

    return instructions_list

instruction_list = read_and_parse_file('2025/test.txtg')

# Part 1
# num_of_zeros = 0
# for instruction in instruction_list:
#     if instruction[0] == 'L':
#         x = arrow_pointer
#         x = (x - instruction[1]) % 100
#     else:
#         x = arrow_pointer
#         x = (x + instruction[1]) % 100
#     arrow_pointer = x
#     num_of_zeros += 1 if arrow_pointer == 0 else 0
#     print(f'Turn {instruction[0]} {instruction[1]}: Arrow is pointing at {arrow_pointer}')

# print(num_of_zeros)

# Part 2 - count the number of times we pass 0
arrow_pointer = 50
num_of_zeros = 0
for instruction in instruction_list:
    if instruction[0] == 'L':
        if (arrow_pointer - instruction[1] % 100) <= 0 and arrow_pointer != 0:            
            num_of_zeros += 1
        arrow_pointer = (arrow_pointer - instruction[1]) % 100
        num_of_zeros += instruction[1] // 100
    else:
        if (arrow_pointer + instruction[1] % 100) <= 0 and arrow_pointer != 0:
            num_of_zeros += 1
        arrow_pointer = (arrow_pointer + instruction[1]) % 100
        num_of_zeros += instruction[1] // 100
    print(f'Turn {instruction[0]}{instruction[1]}: Arrow is pointing at {arrow_pointer}, number of zeros {num_of_zeros}')          

print(num_of_zeros)

    
