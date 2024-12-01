from collections import Counter


def parse_input(lines):
    list_one = []
    list_two = []

    for line in lines:
        x, y = line.strip().split('   ')
        list_one.append(int(x))
        list_two.append(int(y))

    return list_one, list_two


def solution(lines):
    list_one, list_two = parse_input(lines)
    similarity_scores = []
    counter = Counter(list_two)

    for i in list_one:
        similarity_score = i * counter[i]
        similarity_scores.append(similarity_score)

    return sum(similarity_scores)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
