class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for x in nums:
            if x in num_to_freq:
                num_to_freq[x] += 1
            else:
                num_to_freq[x] = 1
        
        freqs = [0] * (len(nums) + 1)
        for x in num_to_freq.keys():
            freq = num_to_freq[x]
            if freqs[freq] == 0:
                freqs[freq] = [x]
            else:
                freqs[freq].append(x)
        
        curr_k = k
        ret = []
        for i in range(len(nums), -1, -1):
            if freqs[i] == 0:
                continue
            else:
                lst_nums_with_freq_i = freqs[i]
                for x in lst_nums_with_freq_i:
                    if curr_k == 0:
                        return ret
                    else:
                        ret.append(x)
                        curr_k -=  1
        
        return ret





