class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = int(sum(nums) / 2)
        if sum(nums) % 2 == 1:
            return False
        
        n = len(nums)
        # dp[i][j] = Using the first i numbers, can we reach target j
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = [False] * (target + 1)
        
        # base case
        dp[0][0] = True
        if nums[0] <= target:
            dp[1][nums[0]] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][target]
