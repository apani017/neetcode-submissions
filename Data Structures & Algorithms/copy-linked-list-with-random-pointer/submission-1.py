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
        oldSet = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldSet[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldSet[cur]
            copy.next = oldSet[cur.next]
            copy.random = oldSet[cur.random]
            cur = cur.next
        return oldSet[head]