# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/

def minimumPushes(word: str) -> int:
    pushes: int = 0

    for i in range(len(word)):
        if i < 8:
            pushes += 1
        elif i < 16:
            pushes += 2
        elif i < 24:
            pushes += 3
        else:
            pushes += 4
    
    return pushes