
def maxProfit(prices: list[int]) -> int:
    # Step 1: Handle edge case - if prices is empty, no profit is possible
    if not prices:
        return 0

    # Step 2: Initialize variables for DP
    # max_profit tracks the maximum profit achievable so far
    # min_price tracks the minimum price seen so far, initialized to infinity
    max_profit = 0
    min_price = float('inf')

    # Step 3: Iterate through each price to compute max profit
    for price in prices:
        # Update min_price to be the smallest price seen so far
        # This is the best price we could have bought at up to this day
        min_price = min(min_price, price)
        # Update max_profit: either keep the previous max or
        # compute profit by selling at the current price (price - min_price)
        max_profit = max(max_profit, price - min_price)

    # Step 4: Return the maximum profit achievable
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))