numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def replace_word(line: str):
    for digit, word in enumerate(numbers):
        line = line.replace(word, f'{word}{digit}{word}')
    return line

def day1(lines: list[str]):
    totalAmount1 = 0

    for line in lines:
        line = line.strip()
        digits = [char for char in line if char.isdigit()]

        if digits:
            totalAmount1 += int(digits[0] + digits[-1])

    totalAmount2 = 0

    for line in lines:
        digits = [char for char in replace_word(line) if char.isdigit()]
        if digits:
            totalAmount2 += int(digits[0] + digits[-1])

    return totalAmount1, totalAmount2

