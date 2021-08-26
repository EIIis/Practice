class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0 # Variable which will hold our current max profit
        for i in range(len(prices)):
            if prices[i] < prices[0]:
                prices[0] = prices[i]
            elif prices[i] - prices[0] > profit:
                profit = prices[i] - prices[0]
        return profit
        