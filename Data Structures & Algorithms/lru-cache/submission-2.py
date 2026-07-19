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


    def _add_node_to_head(self, node: Node):
        prev_node = self.head
        next_node = self.head.next

        prev_node.next = node
        node.next = next_node

        next_node.prev = node
        node.prev = prev_node


    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            curr_node = self.map[key]
            # move it to most recently used
            self._remove_node(curr_node)
            self._add_node_to_head(curr_node)

            return curr_node.value
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            curr_node = self.map[key]
            # move it to most recently used
            self._remove_node(curr_node)
            self._add_node_to_head(curr_node)
            curr_node.value = value
        else:
            new_node = Node(key, value)
            self._add_node_to_head(new_node)
            self.map[key] = new_node

            if len(self.map) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                self.map.pop(lru_node.key)



            


            

            
        
        
