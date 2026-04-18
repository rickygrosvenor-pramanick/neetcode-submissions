class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            curr_target = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == curr_target:
                    to_add = (nums[i], nums[j], nums[k])
                    if to_add in ret:
                        j += 1
                        k -= 1
                    else:
                        ret.add(to_add)
                elif nums[j] + nums[k] > curr_target:
                    k -= 1
                else:
                    j += 1
        
        return [list(x) for x in ret]

