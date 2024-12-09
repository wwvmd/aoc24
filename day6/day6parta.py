import pandas as pd

if __name__ == "__main__":
    file_path = 'day6/input/test.txt'
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    df = None
    facing = 'UP'
    array_2d = [line.strip().split() for line in lines]
    for row in array_2d:
        print(row)
        df = pd.DataFrame(array_2d)
        print(df)
        df = pd.DataFrame([list(line.strip()) for line in lines])
    print(df)
 
    print(df.iloc[6, 4])




    def move(direction,df,x, y):

        #Before moving check if the next position


        if df.iloc[x-1, y] == '#':
            print('Cannot move to this position')
            return False
        

        #When moving up you want stay in the same column but move up a row
        #replace the current position with a  X
        df.iloc[x, y] = 'X'
        df.iloc[x - 1, y] = '^'


    move(df, 6, 4)
    print(df)
