class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = {x for x in nums}
        
        max_len = 0
        for x in nums:
            if x - 1 not in hash_set:
                length = 1
                while x + length in hash_set:
                    length += 1
                max_len = max(max_len, length)

        return max_len