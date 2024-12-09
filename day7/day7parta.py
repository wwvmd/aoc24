
from itertools import product
from functools import reduce
from operator import add, mul

def read_input(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            first_value = int(parts[0])
            other_values = tuple(map(int, parts[1].split()))
            result.append((first_value, *other_values))
    return result

def check_eq(eq, operators):
    test_val, nums = eq[0], eq[1:]
    for ops in product(operators, repeat=(len(nums) - 1)):
        print(ops)
        if (
            reduce(
                lambda acc, x:x[0](acc, x[1]), zip(ops, nums[1:]), nums[0])
            == test_val
        ):
            return True
    return False


def apply_operator(acc, x):
    print(f'acc: {acc} x: {x}')
    foo = x[0](acc, x[1])   
    print(f'foo: {foo}') 
    return foo


def evaluate(item):
    # Placeholder implementation of evaluate function
    # target_result = item[0]
    # numbers = item[1:]
    print(f'doing item: {item}')
    return check_eq(item, [add, mul]) 

if __name__ == "__main__":
    file_path = 'day7/input/real.txt'
    data = read_input(file_path)
    print(data)

    total_right = 0
    for item in data:
        result = evaluate(item)
        print(f'item: {item} result: {result}')
        if result:
            total_right += item[0]

    print(total_right)


