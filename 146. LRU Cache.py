"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 """
class Node:
   def __init__(self, key, val):
      self.key = key
      self.val = val
      self.prev = None
      self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} #map key to node
        
        #Left=LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    #Remove node from list
    def  remove(self, node):
       prev, nxt = node.prev, node.next
       prev.next, next.prev = nxt, prev

    #insert node at right
    def insert(self, node):
       prev, nxt = self.right.prev, self.right
       prev.next = nxt.prev = node
       node.next, node.prev = nxt, prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
           self.remove(self.cache[key])        
           self.insert(self.cache[key])
           return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
           self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self. cache[key])

        if len(self.cache) > self.cap:
           #if is >, remove from list and delete the LRU from hashmap
           lru = self.left.next
           self.remove(lru)
           del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)