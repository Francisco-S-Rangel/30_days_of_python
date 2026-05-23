def add_binary(a: str, b: str) -> str:
    first_value, second_value = int(a, 2), int(b, 2)

    return bin(first_value + second_value)[2:];

print(add_binary("11","1"))
print(add_binary("1010","1011"))
