class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sold = 0
        best_price = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            sold = i
            best_price = max(best_price,prices[sold] - prices[buy])
        return best_price