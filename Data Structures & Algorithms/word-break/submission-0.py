class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[:i] can be segmented into space-separated
        # sequence of dictionary words
        n = len(s)
        dp = [False] * (n + 1)
        # Base Case
        dp[0] = True
        set_words = set(wordDict)

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j : i] in set_words:
                    dp[i] = True
        
        return dp[n]
            