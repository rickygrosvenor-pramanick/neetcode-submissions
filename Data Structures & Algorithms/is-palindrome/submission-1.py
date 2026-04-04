class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""

        s = s.lower()

        for c in s:
            if c.isalnum():
                alpha += c
        
        i = 0
        j = len(alpha) - 1

        while i < j:
            if alpha[i] != alpha[j]:
                return False
            i += 1
            j -= 1
        
        return True