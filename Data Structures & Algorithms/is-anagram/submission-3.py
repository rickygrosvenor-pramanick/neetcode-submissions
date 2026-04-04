class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i not in mapping_s:
                mapping_s[i] = 1
            else:
                mapping_s[i] += 1
        
        for i in t:
            if i not in mapping_t:
                mapping_t[i] = 1
            else:
                mapping_t[i] += 1
        
        t_chars = mapping_t.keys()
        for key in mapping_s.keys():
            if key not in t_chars:
                return False
            s_count = mapping_s[key]
            t_count = mapping_t[key]
            if s_count != t_count:
                return False

        return True

            
            