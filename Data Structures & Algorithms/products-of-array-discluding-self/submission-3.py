class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prod_so_far = 1
        for i in range(len(nums)):
            prefix[i] = prod_so_far
            prod_so_far *= nums[i]
        
        prod_so_far = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod_so_far
            prod_so_far *= nums[i]
        
        ret = []
        for i in range(0, len(nums)):
            ret.append(prefix[i] * suffix[i])
        
        return ret
            