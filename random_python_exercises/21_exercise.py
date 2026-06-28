from typing import List

def plus_one(digits: List[int]) -> List[int]:
    length: int = len(digits) - 1
    newDigits: List[int] = []

    if digits[length] == 9:
        for i in range(length, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        newDigits = [1, *digits]
    else:
        digits[length] += 1
        newDigits = digits

    return newDigits

print(plus_one([9,9,9]))
print(plus_one([9,8,9]))