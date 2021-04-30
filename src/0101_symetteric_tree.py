class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True
