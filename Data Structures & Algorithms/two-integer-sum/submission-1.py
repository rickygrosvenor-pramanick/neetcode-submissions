class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in mapping and mapping[diff] != i:
                return [i, mapping[diff]]
        
