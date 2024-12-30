def max_profit(prices):
    total = 0
    valley = 10 ** 4
    peak = valley

    for i in range(len(prices)):
        if prices[i] < peak:
            total += peak - valley
            valley = prices[i]
            peak = valley
        else:
            peak = prices[i]

    total += peak - valley

    print(total)
    return total

prices = [7, 1, 5, 3, 6, 4]

max_profit(prices)