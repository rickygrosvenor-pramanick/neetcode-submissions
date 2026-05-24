class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_vector_s1 = [0] * 26
        for c in s1:
            freq_vector_s1[ord(c) - ord('a')] += 1
        
        for i in range(0, len(s2) - len(s1) + 1):
            print(i)
            freq_vector_curr = [0] * 26
            current_block = s2[i: i + len(s1)]
            for c in current_block:
                freq_vector_curr[ord(c) - ord('a')] += 1

            equal = True
            for i in range(0, 26):
                if freq_vector_s1[i] != freq_vector_curr[i]:
                    equal = False
            
            if equal is True:
                return True
        
        return False

