import logging
from logging import getLogger, basicConfig


logger = getLogger(__name__)

basicConfig(level=logging.INFO)
logger.setLevel(logging.DEBUG)


def parse_input(lines):
    reports = []
    
    for line in lines:
        report = [int(x) for x in line.strip().split(' ')]
        reports.append(report)

    return reports


def check_if_safe(report):
    result = False
    last_direction = 0

    for i, level in enumerate(report, start=1):
        if i < len(report):
            diff = level - report[i]
            direction = 1 if diff > 0 else -1

            if last_direction and last_direction != direction:
                break
            else:
                last_direction = direction

            if abs(diff) > 0 and abs(diff) <= 3:
                continue
            else:
                break
        
    else:
        result = True

    logger.debug(f'{report} | {result}')
    return result


def solution(lines):
    safe_reports = 0
    reports = parse_input(lines)

    for report in reports:
        if check_if_safe(report):
            safe_reports += 1

    return safe_reports


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        print(solution(lines))
