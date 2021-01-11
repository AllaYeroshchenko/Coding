# 146. LRU Cache

from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.lru.remove(key)
            self.lru.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.lru) == self.capacity:
                deleted = self.lru.popleft()
                del self.cache[deleted]
        else:  
            self.lru.remove(key)
            
        self.lru.append(key)    
        self.cache[key] = value  
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.lru = []

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             if key in self.lru:
#                 self.lru.remove(key)
#                 self.lru.insert(0, key) 
#             return self.cache[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key not in self.cache:
#             if len(self.lru) == self.capacity:
#                 del self.cache[self.lru.pop()]
#                 self.lru.insert(0, key)  
#             else:
#                 #self.lru.append(key)  
#                 self.lru.insert(0, key)
#         else:
#             if key in self.lru:
#                 self.lru.remove(key)
#                 self.lru.insert(0, key) 
            
#         self.cache[key] = value  
        
#         print(self.cache)  
#         print(self.lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)