def my_sqrt(x: int) -> int:
    if x < 2:
        return x

    guess = x

    while True:
        next_value: int = (guess + x / guess) / 2

        if next_value >= guess:
            break

        guess = next_value

    # return guess - (guess % 1)
    return int(guess // 1)

def my_sqrt2(x: int) -> int:
    if x < 2:
        return x

    left: int = 0
    right: int = x // 2

    while left <= right:
        mid: int = (left + right) // 2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(16))
print("\n----------------------\n")
print(my_sqrt2(4))
print(my_sqrt2(8))
print(my_sqrt2(2147395599))