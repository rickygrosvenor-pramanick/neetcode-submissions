class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_of_anagrams = {}

        for x in strs:
            freq_list = [0] * 26
            for c in x:
                index_c = ord(c) - 97
                freq_list[index_c] += 1

            freq_tuple = tuple(freq_list)
            if freq_tuple in group_of_anagrams:
                group_of_anagrams[freq_tuple].append(x)
            else:
                group_of_anagrams[freq_tuple] = [x]
        
        return list(group_of_anagrams.values())
