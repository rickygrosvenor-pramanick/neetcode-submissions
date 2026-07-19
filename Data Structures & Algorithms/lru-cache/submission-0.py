class Node:
    # doubly linkedlist node
    def __init__(self, key=0, value=0):
        # the node needs to know the key too as we need to remove
        # LRU key from self.map
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache:
    # key ideas
    # fast lookups - need a hashmap from key to node object
    # fast evictions and updates - doubly linked list
    def __init__(self, capacity: int):
        # Use a dummy head and tail as otherwise updates may get messy
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}
        self.capacity = capacity
        self.curr_cap = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            curr_node = self.map[key]

            prev_curr = curr_node.prev
            next_curr = curr_node.next
            prev_curr.next = next_curr
            next_curr.prev = prev_curr

            prev_head = self.head.next
            curr_node.next = prev_head
            prev_head.prev = curr_node
            self.head.next = curr_node


            return self.map[key].value
        
    def put(self, key: int, value: int) -> None:
        
        if key not in self.map:
            new_node = Node(key, value)
            if self.curr_cap < self.capacity:
                new_node.next = self.head.next
                self.head.next = new_node
                new_node.prev = self.head
                self.curr_cap += 1
            else:
                lru_node = self.tail.prev
                lru_node.prev.next = self.tail
                self.map.pop(lru_node.key)

                new_node.next = self.head.next
                self.head.next = new_node
                new_node.prev = self.head
        
            self.map[key] = new_node
        else:
            curr_node = self.map[key]
            curr_node.value = value

            prev_curr = curr_node.prev
            next_curr = curr_node.next
            prev_curr.next = next_curr
            next_curr.prev = prev_curr

            curr_node.next = self.head.next
            self.head.next = curr_node
            


            

            
        
        
