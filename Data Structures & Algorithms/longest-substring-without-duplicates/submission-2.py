class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left_ptr = 0
        right_ptr = 0
        seen_so_far = {s[left_ptr]}
        longest_substring = 1

        for i in range(1, len(s)):
            if s[i] in seen_so_far:
                while s[i] in seen_so_far:
                    seen_so_far.remove(s[left_ptr])
                    left_ptr += 1
                seen_so_far.add(s[i])
                right_ptr = i
            else:
                seen_so_far.add(s[i])
                right_ptr = i
            longest_substring = max(longest_substring, right_ptr - left_ptr + 1)

        return longest_substring                
            
