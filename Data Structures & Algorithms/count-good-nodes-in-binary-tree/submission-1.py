# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [(root, float('-inf'))]
        good = 0

        while stk:
            node, big = stk.pop()

            if node.val >= big:
                good += 1

            big = max(big, node.val)

            if node.left:
                stk.append((node.left, big))
            if node.right:
                stk.append((node.right, big))

        return good