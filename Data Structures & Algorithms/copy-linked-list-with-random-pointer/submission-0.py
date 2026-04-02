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
        res = None
        cur1 = res
        hashmap = dict()
        cur = head
        while cur:
            if not res:
                res = Node(cur.val)
                cur1 = res
                
            else:
                cur1.next = Node(cur.val)
                cur1 = cur1.next
            hashmap[cur] = cur1
            cur = cur.next

        #rerun through the original list again
        cur = head
        cur1 = res
        while cur:
            if cur.random:
                cur1.random = hashmap[cur.random]
            cur1 = cur1.next
            cur = cur.next
            
        return res
        