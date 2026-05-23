class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = prices[0]
        right = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            right = prices[i]

            if right - left > max_profit:
                max_profit = right - left
            
            if left > right:
                left = prices[i]
        
        return max_profit