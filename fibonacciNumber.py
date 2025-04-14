
def fib(n):
    # Step 1: Initialize variables for the loop and DP table
    # 'idx' tracks the current Fibonacci number we're computing, starting from F(2)
    # 'sum' will store the current Fibonacci number F(idx)
    # 'preceding' is our DP table, initialized with base cases F(0) = 0 and F(1) = 1
    idx = 2
    sum = 1
    preceding = [0, 1]

    # Step 2: Handle base case for n = 0, return F(0) = 0
    if n == 0:
        return 0

    # Step 3: Handle base case for n = 1, return F(1) = 1
    if n == 1:
        return 1

    # Step 4: Loop from idx = 2 to n to compute F(idx) = F(idx-1) + F(idx-2)
    # For each iteration, calculate the new Fibonacci number, append it to the DP table,
    # and increment idx until we reach F(n)
    while idx <= n:
        # Compute F(idx) by adding the two previous Fibonacci numbers
        sum = preceding[idx - 1] + preceding[idx - 2]
        # Store F(idx) in the DP table for future use
        preceding.append(sum)
        # Move to the next Fibonacci number
        idx += 1

    # Step 5: Return F(n), which is the last computed sum
    return sum

n = 5
print(fib(n))