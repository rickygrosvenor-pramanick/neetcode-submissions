class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        mapping = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # list is not hashable
            count_tuple = tuple(count)
            if count_tuple not in mapping:
                mapping[count_tuple] = [s]
            else:
                mapping[count_tuple].append(s)
        
        for key in mapping.keys():
            ret.append(mapping[key])
        
        return ret
            


