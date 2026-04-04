class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2D DP problem
        # dp[i][j] = True if s[i : j + 1] is a palindrome
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0
        # populate dp array
        for i in range(len(s)- 1, -1, -1):
            for j in range(i, len(s)):
                if j - i == 0:
                    dp[i][j] = True
                    count += 1
                elif j - i == 1:
                    if s[i] == s[j]:
                       dp[i][j] = True
                       count += 1
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                    if dp[i][j] == True:
                        count += 1 
        
        
        return count