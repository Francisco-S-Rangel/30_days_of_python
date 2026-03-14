def in_to_roman(num: int) -> str:
    roman_result: str = ""
    int_values: list[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols: list[str] = ["M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    for index, value in enumerate(int_values):
        while num >= int_values[index]:
            roman_result += roman_symbols[index]
            num -= int_values[index]

    return roman_result

print(in_to_roman(10))
print(in_to_roman(37))
print(in_to_roman(46))
print(in_to_roman(58))
print(in_to_roman(1994))
print(in_to_roman(3749))