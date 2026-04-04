class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        DP1 = [0] * len(nums)
        DP1[0] = nums[0]
        DP1[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            DP1[i] = max(DP1[i - 1], DP1[i - 2] + nums[i])
        
        DP2 = [0] * len(nums)
        DP2[0] = nums[1]
        DP2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            DP2[i] = max(DP2[i - 1], DP2[i - 2] + nums[i + 1])
        
        return max(max(DP1), max(DP2))