# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr_node = head
        while curr_node is not None:
            arr.append(curr_node.val)
            curr_node = curr_node.next
        
        val = arr.pop()
        head = ListNode(val=val, next=None)
        prev = head
        while len(arr) > 0:
            next_node = arr.pop()
            next_node = ListNode(val=val, next=None)
            prev.next = next_node
            prev = next_node
        
        return head
