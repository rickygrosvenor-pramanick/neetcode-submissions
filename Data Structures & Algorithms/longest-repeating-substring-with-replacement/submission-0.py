class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq_map = [0] * 26
        freq_map[ord(s[0]) - ord('a')] = 1
        max_len_substring = 1

        for i in range(1, len(s)):
            right = i
            freq_map[ord(s[right]) - ord("a")] += 1
            most_freq = max(enumerate(freq_map), key=lambda x: x[1])[0]
            window_length = right - left + 1
            letters_to_replace = window_length - most_freq

            while letters_to_replace > k:
                freq_map[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            max_len_substring = max(max_len_substring, right - left + 1)
        
        return max_len_substring
