# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Base case: an empty tree is symmetric
        if root is None:
            return True

        # Helper function to check if two subtrees are mirrors
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # If both nodes are None, they are symmetric
            if left is None and right is None:
                return True
            # If one is None and the other is not None, they are not symmetric
            if left is None or right is None:
                return False
            # Check if values are equal and subtrees are mirrors
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)