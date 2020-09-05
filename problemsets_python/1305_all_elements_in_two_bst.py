"""
Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Solution approach:

1. Implement the classic BFS template recipe.
2. Apply BFS for both the trees.
3. Return the sorted output
"""

from collection import deque

class Solution:
    def get_all_elements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        output = []

        def dfs(root):
            q = deque(root)
            while q:
                node = q.popleft()
                output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        if root1:
            dfs(root1)
        if root2:
            dfs(root2)
        
        return sorted(output)