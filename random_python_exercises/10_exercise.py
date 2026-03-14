def is_power_of_two(n: int) -> bool:
    if n <= 0: return False

    while (n > 0):
        if n % 2 == 1 and n != 1: return False
        n /= 2
    
    return True

print(is_power_of_two(-16))
print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(2))
print(is_power_of_two(3))
print(is_power_of_two(16))