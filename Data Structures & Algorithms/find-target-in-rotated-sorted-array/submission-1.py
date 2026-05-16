class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we want to find minimum, if the target between
        # minimum and nums[n - 1], binary search that half.
        # Or idx = 0, ..., minimum
        def find_min_idx(a, b):

            if a > b:
                return None
            
            mid = (a + b) // 2

            if nums[mid - 1] > nums[mid] and mid - 1 >= 0:
                return mid
            
            if nums[mid] > nums[b]:
                return find_min_idx(mid + 1, b)
            else:
                return find_min_idx(a, mid - 1)
        
        min_idx = find_min_idx(0, len(nums) - 1)
        if min_idx is None:
            min_idx = 0

        def bin_search(a, b):

            if a > b:
                return -1
            
            mid = (a + b) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                return bin_search(mid + 1, b)
            else:
                return bin_search(a, mid - 1)
        
        
        if min_idx == 0:
            return bin_search(0, len(nums) - 1)
        elif nums[min_idx] <= target <= nums[len(nums) - 1]:
            return bin_search(min_idx, len(nums) - 1)
        else:
            return bin_search(0 , min_idx - 1)
            

