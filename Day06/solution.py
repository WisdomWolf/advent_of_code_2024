
direction_map = {
    0: {
        'offset':(-1, 0), 
        'symbol': '^'
    },
    1: {
        'offset': (0, 1), 
        'symbol': '>'
    },
    2: {
        'offset':(1, 0),
        'symbol': 'v'
    },
    3: {
        'offset':(0, -1),
        'symbol': '<'
    }
}


def calc_next_pos(start, current_direction):
    offset = direction_map[current_direction]['offset']
    return (start[0] + offset[0], start[1] + offset[1])


def get_start_pos(lines):
    for i, line in enumerate(lines):
        if '^' in line:
            return (i, line.index('^'))
        

def change_direction(current_direction):
    return current_direction + 1 if current_direction < 3 else 0


def is_obstacle(lines, y, x):
    if not 0 <= y < len(lines) or not 0 <= x < len(lines[0]):
        raise IndexError('Out of bounds index')
    elif lines[y][x] == '#':
        return True
    else:
        return False
    

def update_map(traverse_map, y, x, symbol='X'):
    line = traverse_map[y]
    traverse_map[y] = line[:x] + symbol + line[x + 1:]


def display_map(traverse_map):
    for i, row in enumerate(traverse_map):
        print(f'{i}: {row}')


def parse_input(lines):
    return [line.strip() for line in lines]


def solution(lines):
    lines = parse_input(lines)
    traverse_map = lines.copy()
    current_pos = start_pos = get_start_pos(lines)
    current_direction = 0
    positions = set((current_pos,))
    paths = set()
    paths.add((current_pos, current_direction))

    update_map(traverse_map, *current_pos, symbol='S')

    print(f'Start: {current_pos}')

    while True:
        symbol = direction_map[current_direction]['symbol']
        # if len(positions) % 100 == 0 or len(positions) > 5200:
        #     print('\n'.join(traverse_map))
        #     print(f'Calulated {len(positions)} positions.')
        #     _ = input(f'Current position: {current_pos} | direction: {symbol}. Continue? ')

        next_pos = calc_next_pos(current_pos, current_direction)
        symbol = direction_map[current_direction]['symbol']
        try:
            if is_obstacle(lines, *next_pos):
                current_direction = change_direction(current_direction)
                continue
            else:
                current_pos = next_pos
                if (current_pos, current_direction) not in paths:
                    positions.add(current_pos)
                    paths.add((current_pos, current_direction))
                    if current_pos != start_pos:
                        update_map(traverse_map, *current_pos, symbol=symbol)
                else:
                    print(f'duplicate path break at {current_pos}')
                    break
        except IndexError:
            print('OOB break')
            break
    
    display_map(traverse_map)
    print('current_pos:', current_pos)
    # print(positions)

    return len(positions)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
