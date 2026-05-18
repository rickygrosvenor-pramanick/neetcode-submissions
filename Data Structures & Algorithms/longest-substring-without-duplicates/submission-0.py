class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        right_ptr = 1

        if s[left_ptr] == s[right_ptr]:
            longest_substring = 1
        else:
            longest_substring = 2

        seen_so_far = set()
        seen_so_far.add(s[0])
        seen_so_far.add(s[1])

        for i in range(2, len(s)):
            if s[i] in seen_so_far:
                left_ptr = i
                right_ptr = i
                seen_so_far = set()
                seen_so_far.add(s[i])
                longest_substring = max(longest_substring, 1)
            else:
                seen_so_far.add(s[i])
                right_ptr = i
                longest_substring = max(longest_substring, right_ptr - left_ptr + 1)

        return longest_substring                
            
