import pandas as pd

# Read the file and create a DataFrame
with open('2025/day4_real.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

df = pd.DataFrame(lines)
df.columns = range(len(df.columns))

print(df)
shape = df.shape

print(f'rows: {shape[0]}')
print(f'cols: {shape[1]}')

def check_adjacent_cells(df,row,col):

    



    def get_adjacent_positions(max_rows, max_cols, row, col):
        return [
            df.iloc[row - 1, col] == '@' if row - 1 >= 0 else False,     # Up
            df.iloc[row + 1, col] == '@' if row + 1 < max_rows else False,     # Down
            df.iloc[row, col - 1] == '@' if col - 1 >= 0 else False,     # Left
            df.iloc[row, col + 1] == '@' if col + 1 < max_cols else False,     # Right
            df.iloc[row - 1, col - 1] == '@' if row - 1 >= 0 and col - 1 >= 0 else False, # Up-Left
            df.iloc[row - 1, col + 1] == '@' if row - 1 >= 0 and col + 1 < max_cols else False, # Up-Right
            df.iloc[row + 1, col - 1] == '@' if row + 1 < max_rows and col - 1 >= 0 else False, # Down-Left
            df.iloc[row + 1, col + 1] == '@' if row + 1 < max_rows and col + 1 < max_cols else False  # Down-Right
        ]

    adjacent_positions = get_adjacent_positions(df.shape[0], df.shape[1], row, col)
    print(f'df[{row}, {col}] adjacent positions: {adjacent_positions}')
    if adjacent_positions.count(True) < 4:
        return 1
    return 0




# Example operation: Count occurrences of each character in the DataFrame
countof = 0;
for index, row in df.iterrows():
    # print(index, row)
    col_counter = 0;
    for char in row:
        print(f"Character: {char}, Row: {index}, Column: {col_counter}")
        if char == '@':
            countof += check_adjacent_cells(df, index, col_counter)
        col_counter +=  1
print(f'Total numbner of adjacent @: {countof}')
