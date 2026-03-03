def roman_to_int(s: str) -> int:
    int_value: int = 0

    for index, value in enumerate(s):
        if index > 0 and value == "V" and s[index -1] == "I":
            int_value += 3
        elif index > 0 and value == "X" and s[index -1] == "I":
            int_value += 8
        elif index > 0 and value == "L" and s[index -1] == "X":
            int_value += 30
        elif index > 0 and value == "C" and s[index -1] == "X":
            int_value += 80
        elif index > 0 and value == "D" and s[index -1] == "C":
            int_value += 300
        elif index > 0 and value == "M" and s[index -1] == "C":
            int_value += 800
        else:
            match value:
                case "I":
                    int_value += 1
                case "V":
                    int_value += 5
                case "X":
                    int_value += 10
                case "L":
                    int_value += 50
                case "C":
                    int_value += 100
                case "D":
                    int_value += 500
                case "M":
                    int_value += 1000

    return int_value

print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))