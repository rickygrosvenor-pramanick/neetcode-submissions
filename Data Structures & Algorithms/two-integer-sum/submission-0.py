class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(nums):
            index[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # diff is second number such that
            # n + diff = target
            # make sure that diff is not the same as n
            if diff in index and i != index[diff]:
                return [i, index[diff]]
        
        return []