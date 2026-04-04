class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            # immutable data structure to be hashed
            freq_tuple = tuple(freq)
            if freq_tuple in mapping:
                mapping[freq_tuple].append(s)
            else:
                mapping[freq_tuple] = [s]
        
        ret = [x for x in mapping.values()]
        return ret

            


