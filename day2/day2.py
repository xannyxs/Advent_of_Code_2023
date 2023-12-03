import re
from typing import Tuple

colour_values = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def colour_min(line: str) -> int:
    colour_values = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for component in line.split(':')[1].split(';'):
        for count_colour in component.split(','):
            parts = count_colour.strip().split(' ')
            if len(parts) == 2:
                count, colour = parts
                if colour_values[colour] < int(count):
                    colour_values[colour] = int(count)

    return colour_values['red'] * colour_values['blue'] * colour_values['green']


def colour_validator(line: str) -> bool:
    for component in line.split(':')[1].split(';'):
        for count_colour in component.split(','):
            parts = count_colour.strip().split(' ')
            if len(parts) == 2 and colour_values.get(parts[1], 0) < int(parts[0]):
                return False
    return True


def day2(lines: list[str]) -> Tuple[int, int]:
    totalAmount1 = 0
    totalAmount2 = 0
    for line in lines:
        gameId_match = re.search(r'\b\d{1,3}\b', line)
        if gameId_match and colour_validator(line):
            gameId = int(gameId_match.group())
            totalAmount1 += gameId

        if gameId_match:
            totalAmount2 += colour_min(line)

    return totalAmount1, totalAmount2
