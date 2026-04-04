class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2D DP dictionary Initialisation
        # Using a Dictionary as we can have negative sums
        # dp[i, s] = Starting at index i, how many ways can we reach s.
        dp = {}
        # init base case
        total = sum(nums)
        for s in range(-total, total + 1):
            # if we found target using each num once, set it to 1
            dp[(len(nums), s)] = 1 if s == target else 0
        
        for i in range(len(nums) -1, -1, -1):
            for s in range(-total, total + 1):
                dp[(i, s)] = dp.get((i+1, s - nums[i]), 0) + dp.get((i+1, s + nums[i]), 0)
        
        return dp[(0, 0)]
        
        

        