import pandas as pd

# Read each line of input/test.txt into a pandas Series
file_path = 'day2/input/test.txt'

with open(file_path, 'r') as file:
    lines = [line.split() for line in file.readlines()]
    print(lines)




# data_series = pd.Series(open(file_path).read().splitlines())

# print(data_series)

# for index, row in data_series.iteritems():
#     print(f"Index: {index}, Row: {row}")

# for value in data_series:
#     print(f"Value: {value}")