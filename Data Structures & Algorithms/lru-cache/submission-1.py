class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left = Node(0, 0)   # LRU конец
        self.right = Node(0, 0)  # MRU конец
        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node):  # всегда вставляем перед right
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])   # убираем
            self.insert(self.cache[key])   # ставим в MRU
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   # убираем старый
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])       # вставляем в MRU
        
        if len(self.cache) > self.capacity:
            lru = self.left.next           # самый старый
            self.remove(lru)
            del self.cache[lru.key]

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
