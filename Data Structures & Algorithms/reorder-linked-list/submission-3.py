# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Calculate Length
        org_head = head
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None
        
        # 2. Find Midpoint
        mid_idx = length // 2

        prev = None
        curr = head
        counter = 0
        while counter < mid_idx:
            temp = curr
            counter += 1
            curr = curr.next
            prev = temp

        # 3. Split into first half and second half.
        # curr points to the middle element now
        prev.next = None
        head1 = head
        head2 = curr
        # 4. Reverse second half of the array.
        prev = None
        curr = head2

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # prev is the head of the reversed array

        # 5. Alternate to build the final list
        final = head1
        head1 = head1.next
        head2 = prev
        for i in range(length):
            if i % 2 == 0:
                if head1 is None:
                    break
                final.next = head2
                head2 = head2.next
            else:
                if head2 is None:
                    break
                final.next = head1
                head1 = head1.next
            final = final.next
               
        if head1 is None and head2 is not None:
            final.next = head2
        elif head1 is not None and head2 is None:
            final.next = head1

        head = org_head

        
                


        
        
