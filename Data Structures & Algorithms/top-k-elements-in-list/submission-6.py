class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # an integer can only show up len(nums) times
        freqs = [0] * (len(nums) + 1)
        freq_maps = {}
        
        for num in nums:
            if num in freq_maps:
                freq_maps[num] += 1
            else:
                freq_maps[num] = 1
        
        for num in nums:
            if freqs[freq_maps[num]] != 0:
                freqs[freq_maps[num]].add(num)
            else:
                freqs[freq_maps[num]] = {num}
        
        ret = []
        for i in range(len(nums), -1, -1):
            if freqs[i] != 0:
                ret += list(freqs[i])

        
        return ret[: k]