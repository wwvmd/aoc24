import re


def parse_mull(match):
    numbers = re.findall(r'\d+', match)
    return int(numbers[0]), int(numbers[1])

#txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('day3/input/real.txt', 'r') as file:
    txt = file.read()










matches = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", txt)

sum = 0
perform = True
for match in matches:
    if match == "don't()":
        perform = False
    elif match == "do()":
        perform = True
    else:
        if perform:
            x,y = parse_mull(match)
            sum += x * y       


print(sum)

