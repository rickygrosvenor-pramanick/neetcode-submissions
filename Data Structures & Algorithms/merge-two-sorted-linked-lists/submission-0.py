# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
            
        curr1 = list1
        curr2 = list2

        list_head = None
        if curr1.val > curr2.val:
            list_head = curr2
            curr2 = curr2.next
        else:
            list_head = curr1
            curr1 = curr1.next
        
        head = list_head

        while curr1 is not None and curr2 is not None:
            if curr1.val > curr2.val:
                next_node = curr2.next
                list_head.next = curr2
                list_head = curr2
                curr2 = next_node
            else:
                next_node = curr1.next
                list_head.next = curr1
                list_head = curr1
                curr1 = next_node
        
        if curr1 is None and curr2 is not None:
            list_head.next = curr2
        elif curr1 is not None and curr2 is None:
            list_head.next = curr1
        
        return head
