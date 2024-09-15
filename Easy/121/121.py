def maxProfit(self, prices: list[int]) -> int:
    maxProfit = 0
    buy = prices[0]

    for x in prices:
        if (x - buy) > maxProfit:
            maxProfit = x - buy

        if x < buy:
            buy = x
    
    return maxProfit