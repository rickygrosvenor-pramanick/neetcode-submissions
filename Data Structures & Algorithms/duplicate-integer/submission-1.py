class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        mapping = {}
        for i in nums:
            string = i
            if string not in mapping:
                mapping[string] = 1
            else:
                mapping[string] += 1
        
        max_val = max(mapping.values())
        if max_val > 1:
            return True
        return False
    