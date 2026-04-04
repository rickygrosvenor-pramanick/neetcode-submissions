class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        
        if len(s) >= 1 and s[-1] != "0" :
            dp[-1] = 1
        
        if len(s) >= 2 and s[-2] != "0" :
            if s[-1] == "0" and int(s[-2] + s[-1]) <= 26:
                dp[-2] = 1
            elif int(s[-2] + s[-1]) > 26:
                dp[-2] = 1
            else:
                dp[-2] = 2
        
        for i in range(len(s) - 3, -1, -1):
            if s[i] == "0":
                dp[i] = 0 
            elif int(s[i] + s[i+1]) <= 26:
                if s[i + 1] == 0:
                    dp[i] = dp[i + 2]
                else:
                    dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        
        return dp[0]
                
            

            