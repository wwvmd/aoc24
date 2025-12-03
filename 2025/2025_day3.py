with open('2025/day3_real.txt', 'r') as f:
    data = f.readlines()
    sum = 0
    for line in data:
        # print(line.strip())
        char_array = [int(char) for char in line.strip() if char.isdigit()]
        print(char_array)

        max_index = char_array.index(max(char_array))
        # print(max_index)
        if max_index == len(char_array) - 1:
            print("No larger neighbor to the right")
            new_array = char_array[:-1]
            highest_possible = f'{max(new_array)}{max(char_array)}'
            print(int(highest_possible))
            sum += int(highest_possible)
        else:
            print("Larger neighbor to the right exists")
            highest_possible = f'{max(char_array)}{max(char_array[max_index+1:])}'
            print(int(highest_possible))
            sum += int(highest_possible)
    print("Final Sum:", sum)

