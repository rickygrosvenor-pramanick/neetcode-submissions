class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # detect cycle - floyd's cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # We have detected a collision

        # Find the Loop Entrance - Duplicate Number
        # P = C - X

        slow = 0
        # fast remains at collison point
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        
        return slow