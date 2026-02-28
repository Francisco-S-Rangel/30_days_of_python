def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    mirror_x = int("".join(list(reversed(str(x)))))
    if x == mirror_x: 
        return True
    else:
        return False
    
def is_palindrome_improved(x: int) -> bool:
    if x < 0:
        return False
    mirror_x = int("".join(reversed(str(x))))
    return x == mirror_x
    
print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))

print("----------")

print(is_palindrome_improved(121))
print(is_palindrome_improved(-121))
print(is_palindrome_improved(10))