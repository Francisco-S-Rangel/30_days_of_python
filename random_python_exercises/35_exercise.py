def check_divisibility(n: int) -> bool:
    numbers: str = str(n)
    sum_of_n: int = 0
    product_of_n: int = 1

    for number in numbers:
        aux: int = int(number)

        sum_of_n = sum_of_n + aux
        product_of_n = product_of_n * aux

    return n % (sum_of_n + product_of_n) == 0

print(check_divisibility(99))
print(check_divisibility(10))
print(check_divisibility(23))