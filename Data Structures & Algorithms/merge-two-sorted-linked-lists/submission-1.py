# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a placeholder dummy node
        dummy = ListNode(-1)
        tail = dummy
        
        # 2. Your core traversal logic (cleaned up)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move our output tracker forward
            
        # 3. Attach the remaining tail instantly (replaces your final if/elifs)
        if list1 is not None:
            tail.next = list1 
        else:
            tail.next = list2
        
        # 4. The real head is the node right after our dummy placeholder
        return dummy.next
