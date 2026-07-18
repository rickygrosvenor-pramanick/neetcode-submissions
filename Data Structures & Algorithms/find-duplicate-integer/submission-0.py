class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        slow = nums[0]
        fast = nums[1]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        
        return slow