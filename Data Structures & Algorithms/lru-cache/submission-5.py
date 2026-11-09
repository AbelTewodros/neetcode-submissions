class Node:
    def __init__(self, value = 0,key=None, prev = None, nxt = None):
        self.val = value
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_tail(self.cache[key])
            return self.cache[key].val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_tail(self.cache[key])
        else:
            new_node = Node(value,key)
            self.cache[key] = new_node
            self.tail.prev.nxt = new_node
            new_node.prev = self.tail.prev
            new_node.nxt = self.tail
            self.tail.prev = new_node
            self.used += 1
            if self.used > self.capacity:
                self.remove_old()

        
    def move_to_tail(self,node: int):
        if node.nxt == self.tail:
            return
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.tail.prev.nxt = node
        node.prev = self.tail.prev
        node.nxt = self.tail
        self.tail.prev = node
    def remove_old(self):
        to_remove = self.head.nxt
        self.head.nxt = to_remove.nxt
        to_remove.nxt.prev = self.head
        self.cache.pop(to_remove.key)


