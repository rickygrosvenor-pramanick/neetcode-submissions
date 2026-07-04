# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1.next
        curr_l2 = l2.next
        new_sum = l1.val + l2.val
        new_head_val_node = new_sum % 10
        if new_sum > new_head_val_node:
            carry = 1
        else:
            carry = 0

        new_head = ListNode(val=new_head_val_node)
        curr = new_head

        while curr_l1 or curr_l2 or carry == 1:
            new_sum = carry

            if curr_l1:
                new_sum += curr_l1.val
                curr_l1 = curr_l1.next
            
            if curr_l2:
                new_sum += curr_l2.val
                curr_l2 = curr_l2.next
            
            new_head_val_node = new_sum % 10
            if new_sum > new_head_val_node:
                carry = 1
            else:
                carry = 0
            
            new_node = ListNode(new_head_val_node)
            curr.next = new_node
            curr = curr.next

        
        return new_head


