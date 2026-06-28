# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for i in range(n):
            fast = fast.next
        
        # fast is now n spots away from head

        # if fast is none, then the length of the list = n, so return element after head
        if fast is None:
            return head.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head