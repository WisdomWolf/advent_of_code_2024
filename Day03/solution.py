import regex as re


def mul(x, y):
    return x * y


def first_pass(lines):
    split_lines = re.split(r"don't\(\)", lines[0])
    
    # Add initial chunk since enabled by default
    results = [split_lines[0]]

    for line in split_lines[1:]:
        results.extend(re.findall(r"(?<=do\(\)).*", line))

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
