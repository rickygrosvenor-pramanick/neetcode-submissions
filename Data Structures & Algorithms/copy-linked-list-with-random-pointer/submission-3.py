"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1. Interweave the List A->B->C to A->A'->B->B'->C->C'
        curr = head
        while curr is not None:
            # curr is always an original node in this
            curr_cloned  = Node(curr.val)
            if curr.next is not None:
                curr_cloned.next = curr.next
                curr.next = curr_cloned
                curr = curr_cloned.next
            else:
                curr.next = curr_cloned
                break
        

        # 2. Set the random pointers
        curr = head
        while curr is not None:
            # each original node's next object is its clone, hence curr.random.next
            # curr is always original node
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 3. Unweave the list (Restore Original too - Otherwise Tests Fail)
        curr = head
        new_head = head.next

        while curr is not None:
            curr_cloned = curr.next
            
            # 1. Detach Original from Clone
            curr.next = curr_cloned.next

            # 2. Detatch Clone from Next Original (if it exists)
            if curr_cloned.next is not None:
                curr_cloned.next = curr_cloned.next.next
            
            # this points to the next original as we detached original from clone
            curr = curr.next

        return new_head