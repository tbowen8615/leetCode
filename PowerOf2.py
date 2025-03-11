
def isPowerOfTwo(n):
    # Base case: if n is less than or equal to 0, it can't be a power of 2
    if n <= 0:
        return False
    # Base case: if n is 1, it is a power of 2 (2^0 = 1)
    if n == 1:
        return True
    # If n is odd and not 1, it can't be a power of 2
    if n % 2 != 0:
        return False
    # Recursive case: divide n by 2 and check the result
    return isPowerOfTwo(n // 2)

n = 1
print(isPowerOfTwo(n))

n = 4
print(isPowerOfTwo(n))

n = 7
print(isPowerOfTwo(n))
