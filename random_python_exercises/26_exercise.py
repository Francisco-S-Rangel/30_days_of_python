def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    
    if n <= 2:
        return 1
    
    t1: int = 0
    t2: int = 1
    t3: int = 1
    next_term: int = t1 + t2 + t3

    for i in range(2, n):
        next_term = t1 + t2 + t3
        t1 = t2
        t2 = t3
        t3 = next_term

    return next_term