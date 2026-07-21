def fib(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
        
    f1: int = 1
    f2: int = 1
    next_fib: int = f1 + f2

    for i in range(2, n):
        next_fib = f1 + f2
        f1 = f2
        f2 = next_fib

    return next_fib

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))