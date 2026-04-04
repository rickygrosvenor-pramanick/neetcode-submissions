class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies of each number - O(n)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # Use Bucket Sort Algorithm - Make Buckets for frequencies 1 to n (0 idx unused)
        buckets = [[] for _ in range(len(nums)+1)]

        # For each num in nums, append them to the list at index count - O(n)
        for key in freq.keys():
            count = freq[key]
            buckets[count].append(key)
        
        # ret = []
        # i = 0
        # while k > 0:
        #     arr = buckets[len(nums) - i]
        #     if len(arr) == 0:
        #         i += 1
        #         continue
        #     elif len(arr) <= k:
        #         for x in arr:
        #             ret.append(x)
        #         k -= len(arr)
        #     else:
        #         slice_to_take = arr[:k]
        #         for x in slice_to_take:
        #             ret.append(x)
        #         k = 0
            
        #     i += 1
        
        # return ret
        ret = []
        for i in range(len(nums), -1, -1):
            curr_bucket = buckets[i]
            if len(curr_bucket) == 0:
                continue
            for x in curr_bucket:
                if len(ret) == k:
                    return ret
                ret.append(x)
            if len(ret) == k:
                    return ret

        return 


                

