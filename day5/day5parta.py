def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    dictionary = {}
    array = []
    blank_line_found = False

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            blank_line_found = True
            continue

        if not blank_line_found:
            key, value = stripped_line.split('|')
            dictionary[key.strip()] = value.strip()
        else:
            array.append(stripped_line)

    return dictionary, array

if __name__ == "__main__":
    file_path = 'day5/input/test.txt'
    dictionary, array = read_file(file_path)
    print("Dictionary:", dictionary)
    print("Array:", array)