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
    file_path = 'day1/input/real.txt'
    series1, series2 = read_and_parse_file(file_path)
    print("Series 1:", series1)
    print("Series 2:", series2)

    series1_sorted = sorted(series1)
    series2_sorted = sorted(series2)

    print("Series 1 Sorted:", series1_sorted)
    print("Series 2 Sorted:", series2_sorted)


    differences = []
    for s1, s2 in zip(series1_sorted, series2_sorted):
        differences.append(abs(int(s1) - int(s2)))


    total_difference = sum(differences)
    print("Total Difference:", total_difference)        

