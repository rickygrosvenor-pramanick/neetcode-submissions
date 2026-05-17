class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_window = 101
        right_window = 101
        max_profit_so_far = 0

        for i in range(len(prices)):
            if left_window > prices[i]:
                left_window = prices[i]
                right_window = prices[i]

            right_window = max(prices[i], right_window)
            
            max_profit_so_far = max(max_profit_so_far, right_window - left_window)
        
        return max_profit_so_far