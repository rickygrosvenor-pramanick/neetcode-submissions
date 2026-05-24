# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(1) Space Algorithm - Floyd's Cycle-Finding Algorithm
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False



        # O(n) Space Algorithm
        # visited = set()
        # curr = head

        # while curr is not None:
        #     if curr not in visited:
        #         visited.add(curr)
        #         curr = curr.next
        #     else:
        #         return True
        
        # return False