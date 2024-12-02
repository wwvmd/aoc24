import pandas as pd

def compare(a, b, asc):
    if asc is None:
        asc = a < b
    
    ## if asc then a - b should be negative

    if asc and a > b:
        is_safe = False
    elif not asc and a < b:
        is_safe = False
    else:
        is_safe = abs(a - b) >= 1 and abs(a - b) <= 3
    return is_safe, asc

# Read each line of input/test.txt into a pandas Series
file_path = 'day2/input/test.txt'

with open(file_path, 'r') as file:
    lines = [line.split() for line in file.readlines()]
    #print(lines)
    safe_count = 0
    for lin in lines:
        asc = None
        is_safe = None
        for i in range(len(lin)):
            #print(lin[i])
            next = i+1
            if next > len(lin)-1:
                break
            is_safe, asc =  compare(int(lin[i]), int(lin[next]),asc)           
            if not is_safe:
                break
        if is_safe:
            safe_count += 1
    print(safe_count)

# data_series = pd.Series(open(file_path).read().splitlines())

# print(data_series)

# for index, row in data_series.iteritems():
#     print(f"Index: {index}, Row: {row}")

# for value in data_series:
#     print(f"Value: {value}")