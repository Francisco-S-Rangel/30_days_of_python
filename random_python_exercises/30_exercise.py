from typing import List

def sequential_digits(low: int, high: int) -> List[int]:
    all_possible_digits: List[int] = [
        12,       23,       34,        45,
        56,       67,       78,        89,
        123,      234,      345,       456,
        567,      678,      789,      1234,
        2345,     3456,     4567,      5678,
        6789,    12345,    23456,     34567,
        45678,    56789,   123456,    234567,
        345678,   456789,  1234567,   2345678,
        3456789, 12345678, 23456789, 123456789
    ]
    digits: List[int] = []

    for value in all_possible_digits:
        if high < value:
            break

        if value >= low and value <= high:
            digits.append(value)

    return digits

def sequential_digits(low: int, high: int) -> List[int]:
    all_possible_digits: List[int] = []

    for i in range (1, 10):
        sum_string: str = str(i)
        for j in range(i + 1, 10):
            sum_string += str(j)
            all_possible_digits.append(int(sum_string))
        
    return sorted([value for value in all_possible_digits if low <= value <= high])

def sequential_digits(low: int, high: int) -> List[int]:
    all_possible_digits: List[int] = []

    for i in range (1, 10):
        value = i
        for j in range(i + 1, 10):
            value = value * 10 + j
            if low <= value <=  high:
                all_possible_digits.append(value)
        
    return sorted(all_possible_digits)
