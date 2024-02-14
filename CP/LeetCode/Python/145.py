# 145. Binary Tree Postorder Traversal

from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        # Time Complexity of recursive solution is O(n) and Space Complexity is O(n)

        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # ---
        # Time Complexity of iterative solution is O(n) and Space Complexity is O(n)

        res = []
        stack = [root] if root else []

        while stack:
            _root = stack.pop()
            res.append(_root.val)
            if _root.left:
                stack.append(_root.left)
            if _root.right:
                stack.append(_root.right)

        return res[::-1]


if __name__ == "__main__":
    new_root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    sol = Solution()

    print(sol.postorderTraversal(new_root))
