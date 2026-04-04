class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] = num combinations using first i coins to get amount j
        # init dp
        n = len(coins)
        dp = [0] * (n + 1)
        for i in range(0, n + 1):
            dp[i] = [0] * (amount + 1)
        
        # base case
        dp[0][0] = 1

        # Top Case: We either dont use current coin and see how many combinations that give us.
        # This is denoted by dp[i - 1][j].
        # Or we iterate through all coins less or equal to target value and see how many combinations
        # that gives us. This is denoted by dp[i][j - coins[i]] for all i where j - coins[i] >=0.
        # We keep dp[i] in the second case as we can reuse coins - unbounded knapsack.

        # recurrence: dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]] for all i where j - coins[i] >=0
        # dp[i][j] = dp[i - 1][j] if coins[i] > j
        # dp[i][j] = 0 for else (settled in base case)

        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        
        return dp[n][amount]

