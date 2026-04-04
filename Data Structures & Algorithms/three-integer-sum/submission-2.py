class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums) - 2):
            curr_num = nums[i]
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                total = curr_num + nums[j] + nums[k]
                if total == 0:
                    ret.append([curr_num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        
        return ret