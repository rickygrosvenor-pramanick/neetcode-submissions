class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def search_idx(start, end):
            if start > end:
                return -1
                
            if start == end and nums[start] == target:
                return start
        
            mid = (end + start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return search_idx(mid + 1, end)
            else:
                return search_idx(start, mid - 1)

            return -1

        return search_idx(0, len(nums) - 1) 