class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = {x for x in nums}

        max_so_far = 1
        for i in range(0, len(nums)):
            count = 1
            if nums[i] - 1 not in set_nums:
                curr = nums[i]
                while curr + 1 in set_nums:
                    curr += 1
                    count += 1
                
                max_so_far = max(max_so_far, count)
        
        return max_so_far
                