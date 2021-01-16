#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    
    def _init_(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, insert_node, index_node):
        prev_node = index_node.prev
        prev_node.next = insert_node
        insert_node.next = index_node
        insert_node.prev = prev_node
        index_node.prev = insert_node

    def removeNode(self, remove_node):
        remove_node.prev.next = remove_node.next
        remove_node.next.prev = remove_node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.map = {}
        self.dll = DLL() 

    def get(self, key: int) -> int:

        if key in self.map.keys():
            node = self.map[key]
            # remove LRU
            self.dll.removeNode(node)
            # add the new node to MRU
            self.dll.insertNode(node, self.dll.tail)
            return self.map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # create new node 
        node = Node()
        node.val = value
        node.key = key
        if key in self.map.keys():
            # remove the old node
            self.dll.removeNode(self.map[key])
        elif self.length >= self.capacity:    
            lru = self.dll.head.next
            # remove old key
            del self.map[lru.key]
            # remove LRU
            self.dll.removeNode(lru)
        else:
            self.length += 1
        # add the new node to MRU
        self.dll.insertNode(node, self.dll.tail)
        # update map
        self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

