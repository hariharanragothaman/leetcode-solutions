from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result

        stack = [(root, [root.val], root.val)]

        while stack:
            node, path, value = stack.pop()
            if not node.left and not node.right:
                if value == targetSum:
                    result.append(path)
            if node.left:
                stack.append((node.left, path + [node.left.val], node.left.val + value))
            if node.right:
                stack.append(
                    (node.right, path + [node.right.val], node.right.val + value)
                )
        return []
