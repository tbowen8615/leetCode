
def fib(n):
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 5
print(fib(n))