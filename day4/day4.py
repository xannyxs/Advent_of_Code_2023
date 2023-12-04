import re
import numpy
from typing import Tuple, Dict

amount_of_cards: Dict[int, int] = {}


def calculate_card_value(number_of_matches: int) -> int:
    if number_of_matches == 0:
        return 0

    value = 1
    for _ in range(1, number_of_matches):
        value *= 2

    return value


def day4(lines: list[str]) -> Tuple[int, int]:
    totalAmount1 = sum(calculate_card_value(len(numpy.intersect1d(re.findall(r"(\d+)", line[(line.find(':') + 2):(line.find('|') - 1)]),
                                                                  re.findall(r"(\d+)", line[(line.find('|') + 2):])))) for line in lines)
    for i, line in enumerate(lines, 1):
        yourNumbers = re.findall(
            r"(\d+)", line[(line.find(':') + 2):(line.find('|') - 1)])
        winningNumbers = re.findall(r"(\d+)", line[(line.find('|') + 2):])

        listOfNumbers = len(numpy.intersect1d(yourNumbers, winningNumbers))
        for r in range(1, listOfNumbers + 1):
            amount_of_cards[i] = amount_of_cards.get(i, 0)
            amount_of_cards[r + i] = amount_of_cards.get(r + i, 0)

            amount_of_cards[r + i] += 1 + amount_of_cards[i]

    return totalAmount1, sum(amount_of_cards.values()) + len(lines)
