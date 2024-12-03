import re


def mul(x, y):
    return x * y


def parse_input(lines):
    results = []
    for line in lines:
        results.extend(re.findall(r'mul\(\d+,\d+\)', line))

    return results


def solution(lines):
    parsed = parse_input(lines)
    result = 0
    for i in parsed:
        result += eval(i)

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
