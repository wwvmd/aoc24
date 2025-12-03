def is_mirror_halves(n):
    s = str(n)
    length = len(s)
    
    # If odd length, return False (can't split evenly)
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

def count_repeated_patterns(n):
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the string length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeat_count = length // pattern_len
            
            # Check if the pattern repeats throughout the entire string
            if pattern * repeat_count == s and repeat_count >= 2:
                return repeat_count
    
    return 0

with open('2025/day2_real.txt', 'r') as file:
    lines = file.readlines()
    id_ranges = lines[0].split(',')
    total = 0
    print(id_ranges)
    for id_range in id_ranges:
        ids = id_range.split('-')
        id_range = int(ids[0]),int(ids[1])
        print(id_range)
        count = 0
        for i in list(range(id_range[0], id_range[1] + 1)):
            print(i)
            if count_repeated_patterns(i) > 0:
                count += count_repeated_patterns(i) 
                total += i
        print(f'For ID range {id_range}, total repeated patterns: {count}')
    print(f'Grand total of all mirror halves IDs: {total}')

