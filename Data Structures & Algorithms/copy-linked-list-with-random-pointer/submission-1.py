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
        
        # 3. Unweave the list
        curr = head.next
        new_head = head.next

        while curr is not None:
            # curr is always cloned node 
            # if curr.next is not None, then next original node exists
            # so we bounce to the next cloned node
            if curr.next is not None:
                next_cloned = curr.next.next
                curr.next = next_cloned
                curr = next_cloned
            else:
                break
        
        return new_head