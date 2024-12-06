from collections import defaultdict
from functools import cmp_to_key


def compare_nodes(this, other):
    # -1 for less than, 0 for equal, 1 for more
    left = rule_map[this]['left']
    right = rule_map[this]['right']

    if left and other in left:
        return 1
    elif right and other in right:
        return -1
    else:
        return 0


def node_factory():
    return {'left': [], 'right': []}


rule_map = defaultdict(node_factory)


def build_map(rules):
    global rule_map

    for i, j in rules:
        rule_map[i]['right'].append(j)
        rule_map[j]['left'].append(i)


def parse_input(lines):
    rules = []
    updates = []

    for line in lines:
        if '|' in line:
            rules.append([int(x) for x in line.strip().split('|')])
        elif ',' in line:
            updates.append([int(x) for x in line.strip().split(',')])
        else:
            continue

    build_map(rules)
    return updates


def is_valid_update(update):
    valid = False

    for next_index, page in enumerate(update, start=1):
        if next_index >= len(update):
            continue
        else:
            next_page = update[next_index]

        if next_page in rule_map[page]['right'] \
            or page in rule_map[next_page]['left']:
            continue
        else:
            break
    else:
        valid = True

    return valid


def reorder_update(update):
    return update


def extract_middle_page(update):
    return update[len(update) // 2]


def solution(lines):
    result = 0
    updates = parse_input(lines)

    for update in updates:
        if not is_valid_update(update):
            update = sorted(update, key=cmp_to_key(compare_nodes))
            result += extract_middle_page(update)

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
