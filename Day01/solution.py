def solution(lines):
    list_one = []
    list_two = []
    distances = []

    for line in lines:
        x, y = line.strip().split('   ')
        list_one.append(int(x))
        list_two.append(int(y))

    for i, j in zip(sorted(list_one), sorted(list_two)):
        distances.append(abs(i - j))

    return sum(distances)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
