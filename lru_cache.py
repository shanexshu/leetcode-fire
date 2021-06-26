class ListNode:
    def __init__(self, val=0, key=0):
        # nodes will hold the value of the key, as well as the key
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        # dictionary with (key, nodeptr)
        self.dic = {}
        self.cap = capacity
        
        # dummy head and tail nodes
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            # put it at front
            self.remove(node)
            self.add(node)
            
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        newnode = ListNode(value, key)
        if key in self.dic:
            # remove it
            node = self.dic[key]
            self.remove(node)
        
        self.dic[key] = newnode
            
        # put new at front
        self.add(newnode)
            
        # if at cap, evict the tail
        if len(self.dic)>self.cap:
            node = self.tail.prev
            self.remove(node)
            del self.dic[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)