from collections import defaultdict


def node_factory():
    return {'left': [], 'right': []}


def build_map(rules):
    rule_map = defaultdict(node_factory)
    for i, j in rules:
        rule_map[i]['right'].append(j)
        rule_map[j]['left'].append(i)

    return rule_map


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

    return rules, updates


def is_valid_update(update, rule_map):
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


def extract_middle_page(update):
    return update[len(update) // 2]


def solution(lines):
    result = 0
    rules, updates = parse_input(lines)
    rule_map = build_map(rules)

    for update in updates:
        if is_valid_update(update, rule_map):
            result += extract_middle_page(update)

    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
