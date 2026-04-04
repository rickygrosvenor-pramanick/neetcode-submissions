class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums)

        for i in range(0, len(nums)):
            max_subseq_len = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_subseq_len = max(max_subseq_len, DP[j])
                
            DP[i] = 1 + max_subseq_len
        
        return max(DP) - 1