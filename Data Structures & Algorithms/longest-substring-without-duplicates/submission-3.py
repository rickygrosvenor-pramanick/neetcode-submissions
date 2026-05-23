class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen_so_far = {s[left]}
        length = 1

        for i in range(1, len(s)):
            right = i
            while s[right] in seen_so_far:
                seen_so_far.remove(s[left])
                left += 1
            
            seen_so_far.add(s[right])
            length = max(length, right - left + 1)
        
        return length