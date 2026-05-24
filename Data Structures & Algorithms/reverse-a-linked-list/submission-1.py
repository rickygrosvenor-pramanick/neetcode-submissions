# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        curr = head
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        
        new_head_val = arr.pop()
        new_head = ListNode(new_head_val)
        curr = new_head

        while len(arr) > 0:
            next_val = arr.pop()
            next_node = ListNode(next_val)
            curr.next = next_node
            curr = next_node
        
        return new_head
        
