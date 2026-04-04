class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        i = 1
        while i < len(nums):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            i += 1
    

        i = len(nums) - 2
        while i > -1:
            suffix[i] = suffix[i + 1] * nums[i + 1]
            i -= 1
        
        ret = [1] * len(nums)

        for i in range(0, len(nums)):
            ret[i] = prefix[i] * suffix[i]
        
        return ret
