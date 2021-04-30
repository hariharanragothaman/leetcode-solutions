"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                if value == target:
                    return True
            if node.left:
                stack.append((node.left, node.left.val + value))
            if node.right:
                stack.append((node.right, node.right.val + value))
        return False
