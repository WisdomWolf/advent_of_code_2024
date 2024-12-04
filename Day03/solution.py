import regex as re


def mul(x, y):
    return x * y


def first_pass(lines):
    results = []
    for line in lines:
        results.extend(re.findall(r"^.*?(?=don't\(\)|do\(\))", line))
        results.extend(re.findall(r"(?<=do\(\)).*?(?=don't\(\)|do\(\))", line, overlapped=True))
        results.append(re.findall(r"(?<=do\(\)).*(?!don't\(\))", line, overlapped=True)[-1])

    return results


def parse_input(lines):
    results = []

    for s in first_pass(lines):
        results.extend(re.findall(r'mul\(\d+,\d+\)', s))
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
