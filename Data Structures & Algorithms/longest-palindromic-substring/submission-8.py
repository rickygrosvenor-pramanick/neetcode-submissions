class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # init dp array
        dp = [None] * len(s)
        for i in range(len(dp)):
            dp[i] = [False] * len(s)
        
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(0, i):
                dp[i][j] = False
        
        # Populate dp array, build it top-down as needed in recurrence
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                s_slice = s[i: j+1]

                if len(s_slice) == 2:
                    dp[i][j] = bool(s[i] == s[j])
                    continue

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
        
        # Extract Longest Palindromic Substring
        max_len = 0
        start = None
        end = None
        for i in range(len(s)):
            for j in range(len(s) - 1, i , -1):
                if dp[i][j] is True:
                    if max_len < j - i + 1:
                        max_len = j - i
                        start = i
                        end = j
        
        if start is None or end is None:
            return s[0]
            
        return s[start: end + 1]


