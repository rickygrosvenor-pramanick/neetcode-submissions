class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def search(a, b):

            if a > b:
                return None
            
            mid = (a + b) // 2

            # check if the mid + 1 is the minimum
            if mid + 1 <= len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # check if mid is the minimum
            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[b]:
                return search(mid + 1, b)
            else:
                return search(a, mid - 1)
        
        min_num = search(0, len(nums) - 1)

        if min_num is None:
            return nums[0]
        else:
            return min_num
        