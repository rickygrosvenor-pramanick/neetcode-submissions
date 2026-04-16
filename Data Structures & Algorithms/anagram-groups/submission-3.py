class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1

            freq = tuple(freq)
            if freq in groups:
                groups[freq].append(s)
            else:
                groups[freq] = [s]
        
        return list(groups.values())