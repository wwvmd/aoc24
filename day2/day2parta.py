import pandas as pd

def compare(a, b, asc):
    if asc is None:
        asc = a < b

        
    return a < b == asc, asc

# Read each line of input/test.txt into a pandas Series
file_path = 'day2/input/test.txt'

with open(file_path, 'r') as file:
    lines = [line.split() for line in file.readlines()]
    print(lines)

    for lin in lines:
        asc = None
        for i in range(len(lin)):
            print(lin[i])
            next = i+1
            if next > len(lin):
                break
            valid,asc =  compare(lin[i], lin[next],asc)



        print('end of lin')





# data_series = pd.Series(open(file_path).read().splitlines())

# print(data_series)

# for index, row in data_series.iteritems():
#     print(f"Index: {index}, Row: {row}")

# for value in data_series:
#     print(f"Value: {value}")