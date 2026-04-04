class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # # 2D DP dictionary Initialisation
        # # Using a Dictionary as we can have negative sums
        # # dp[i, s] = Starting at index i, how many ways can we reach s.
        # dp = {}
        # # init base case
        # total = sum(nums)
        # for s in range(-total, total + 1):
        #     # if we found target using each num once, set it to 1
        #     dp[(len(nums), s)] = 1 if s == target else 0
        
        # for i in range(len(nums) -1, -1, -1):
        #     for s in range(-total, total + 1):
        #         dp[(i, s)] = dp.get((i+1, s - nums[i]), 0) + dp.get((i+1, s + nums[i]), 0)
        
        # return dp[(0, 0)]
        n = len(nums)
        total = sum(nums)
        DP = [-1] * (n + 1)
        for i in range(n + 1):
            DP[i] = [-1] * (2 * total + 1)
        
        for s in range(2*total + 1):
            DP[n][s] = 0
            if s == target + total:
                DP[n][s] = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(0, 2*total + 1):
                actual = j - total
                DP[i][j] = 0
                if actual - nums[i] >= -total:
                    DP[i][j] += DP[i + 1][actual - nums[i] + total]
                if actual + nums[i] <= total:
                    DP[i][j] += DP[i + 1][actual + nums[i] + total]
        
        return DP[0][total]

        
        

        