class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_vector_s1 = [0] * 26
        window_vector = [0] * 26
        for i in range(len(s1)):
            freq_vector_s1[ord(s1[i]) - ord('a')] += 1
            window_vector[ord(s2[i]) - ord('a')] += 1
        
        if freq_vector_s1 == window_vector:
            return True
        
        for i in range(len(s1), len(s2) - len(s1) + 1):
            window_vector[ord(s2[i - 1]) - ord('a')] -= 1
            window_vector[ord(s2[i]) - ord('a')] += 1
            if freq_vector_s1 == window_vector:
                return True
        
        return False

