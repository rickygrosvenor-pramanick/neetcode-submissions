class Solution:
    def rob(self, nums: List[int]) -> int:
        DP = [0] * len(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max (nums[0], nums[1])
        
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            DP[i] = max(DP[i - 1], nums[i] + DP[i - 2])
        
        return max(DP)