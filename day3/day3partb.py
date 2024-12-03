import re


def parse_mull(match):
    numbers = re.findall(r'\d+', match)
    return int(numbers[0]), int(numbers[1])

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# with open('day3/input/real.txt', 'r') as file:
#     txt = file.read()

#x = re.search("mul\(\d{1,3},\d{1,3}\)", txt)

mul_operators_with_position = [(m.group(), m.start(0), m.end(0)) for m in re.finditer("mul\(\d{1,3},\d{1,3}\)", txt)]

dont_operators_position = [m.start(0) for m in re.finditer("don't", txt)]

do_operators_position = [m.start(0) for m in re.finditer("do()", txt)]


### Iterate over mul_operators_with_position and check if the position
## at the start we are all good we assume do operates

sum = 0
for match, start, end in mul_operators_with_position:
    if not any(dont_start < start < dont_start + 5 for dont_start in dont_operators_position):
        x, y = parse_mull(match)
        sum += x * y

print(sum)





# sum = 0
# for match in matches:
#     x,y = parse_mull(match)
#     sum += x * y

# print(sum)

