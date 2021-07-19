class LRUCache:
    
    def __init__(self, capacity):
        self.cap = capacity
        self.dic = OrderedDict()

    def get(self, key):
        # Return the value of the key if the key exists, otherwise -1.
        if key in self.dic:
            self.dic.move_to_end(key, last=False)
            return self.dic[key]
        return -1

    def put(self, key, value):
        # Update the value of the key if the key exists. 
        # Otherwise, add the key-value pair to the cache. 
        # If the number of keys exceeds the capacity from this operation, 
        # evict the least recently used key.

        self.dic[key] = value
        self.dic.move_to_end(key, last=False)
        if len(self.dic)>self.cap:
            self.dic.popitem(last=True)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)