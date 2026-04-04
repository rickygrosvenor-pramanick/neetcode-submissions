class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s not in map_s:
                map_s[char_s] = 1
            else:
                map_s[char_s] += 1
            
            if char_t not in map_t:
                map_t[char_t] = 1
            else:
                map_t[char_t] += 1
        
        s_chars = map_s.keys()
        t_chars_set = set(map_t.keys())
        for c in s_chars:
            if c not in t_chars_set:
                return False
            
            if map_s[c] != map_t[c]:
                return False
        
        return True
        