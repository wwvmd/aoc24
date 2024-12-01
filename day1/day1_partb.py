def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    series1 = []
    series2 = []
    
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            series1.append(parts[0])
            series2.append(parts[1])
    
    return series1, series2

if __name__ == "__main__":
    file_path = 'day1/input/test.txt'
    series1, series2 = read_and_parse_file(file_path)
    print("Series 1:", series1)
    print("Series 2:", series2)

    series1_sorted = sorted(series1)
    series2_sorted = sorted(series2)

    print("Series 1 Sorted:", series1_sorted)
    print("Series 2 Sorted:", series2_sorted)


    #similiarity_score = element * number of occurences in series2



    differences = []
    similiarity_score = 0 
    for s1 in series1_sorted:
        print(f'element is {s1} and number of occurences is {series2_sorted.count(s1)}')
        element_score = int(s1) * series2_sorted.count(s1)
        similiarity_score += element_score

    print("Similiarity Score:", similiarity_score)


