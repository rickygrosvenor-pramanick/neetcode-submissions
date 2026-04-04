class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums)

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], 1+DP[j])
                
        
        return max(DP)