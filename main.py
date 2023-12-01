from typing import Tuple
from day1.day1 import day1
from utils.read_file import read_file


def print_solution(day: str, solution: Tuple[int, int]) -> None:
    print(day)
    print("Solution 1:", solution[0])
    print("Solution 2:", solution[1])


if __name__ == "__main__":
    lines = read_file('day1/input.txt')

    print_solution('Day 1:', day1(lines))
