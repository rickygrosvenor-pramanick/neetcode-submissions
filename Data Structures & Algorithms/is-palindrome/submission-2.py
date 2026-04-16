class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        split_str = s.split()
        s_without_spaces = ""
        for s in split_str:
            s_without_spaces += s
        
        final_s = ""
        for c in s_without_spaces:
            if c.isalnum():
                final_s += c
        
        i = 0
        j = len(final_s) - 1

        print(final_s)

        while i < j:
            if final_s[i] != final_s[j]:
                return False

            i += 1
            j -= 1
        
        return True
        

        

        