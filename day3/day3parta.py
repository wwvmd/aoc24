import re


def parse_mull(match):
    numbers = re.findall(r'\d+', match)
    return int(numbers[0]), int(numbers[1])

#txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open('day3/input/real.txt', 'r') as file:
    txt = file.read()

x = re.search("mul\(\d{1,3},\d{1,3}\)", txt)

matches = re.findall("mul\(\d{1,3},\d{1,3}\)", txt)
print(matches)


sum = 0
for match in matches:
    x,y = parse_mull(match)
    sum += x * y

print(sum)

