# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, array):
        self.arr = array
        self.root = None

    def create_tree(self, hmap):
        """
        Function that builds the tree
        Returns:
        """
        n = len(self.arr)
        self.root = hmap[0]

        # This is just to assign left and right children
        i = 0
        while i < n:
            node = hmap[i]

            if 0 < (2 * i + 1) < n:
                if arr[2 * i + 1]:
                    node.left = hmap[2 * i + 1]
            else:
                node.left = None

            if 0 < (2 * i + 2) < n:
                if arr[2 * i + 2]:
                    node.right = hmap[2 * i + 2]
            else:
                node.right = None
            i += 1

        return self.root

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # subroutine to get post-order traversal
        def get_post_order(root):
            res_temp = []
            post_order = []

            if not root:
                return 0

            stack = [root]

            while stack:
                root = stack.pop()
                res_temp.append(root)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

            while res_temp:
                post_order.append(res_temp.pop())

            return post_order

        if not root:
            return 0

        postOrder = get_post_order(root)

        count = 0
        for c in postOrder:
            print(c)
            if c.left is None and c.right is None:
                print("Entering here")
                count += 1
                c.val = -1

            if c.left and c.left.val == -1 and c.right and c.right.val == -1:
                count += 1

            print("********************************")
        print(count)
        return count


if __name__ == "__main__":
    arr = [5, 1, 5, 5, 5, None, 5]
    s = Solution(arr)
    node_map = {}
    for i in range(len(arr)):
        node_map[i] = TreeNode(arr[i])
    print("The node map is:", node_map)
    root = s.create_tree(node_map)
    s.countUnivalSubtrees(root)
