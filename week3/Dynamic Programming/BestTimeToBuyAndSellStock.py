
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        if not prices:
            return 0
        if(len(prices) is 2 and prices[0] <= prices[1]):
            return prices[1] - prices[0]
        day_zero = prices[0]
        purchase = 0
        profit = 0
        buy = 0
        sell = 0
        while(i < len(prices)):
            if(prices[i] < day_zero and purchase is 0):
                buy = prices[i]
                purchase = 1
                i += 1
            elif(sell < prices[i]):
                sell = prices[i]
                i += 1
            else:
                i += 1
        if(sell > buy):
            profit = sell - buy
        return profit