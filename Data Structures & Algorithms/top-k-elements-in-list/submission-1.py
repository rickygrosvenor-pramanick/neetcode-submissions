class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        
        vals = list(mapping.values())
        vals.sort(reverse=True)
        ret = []
        num_append = 0
        for val in vals:
            for key in mapping.keys():
                if num_append == k:
                    break
                if mapping[key] == val and key not in ret:
                    ret.append(key)
                    num_append += 1

        
        return ret