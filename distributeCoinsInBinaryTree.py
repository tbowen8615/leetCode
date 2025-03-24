# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # Track total moves
        self.moves = 0

        def helper(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # Post-order traversal: process left and right children first
            left = helper(node.left)
            right = helper(node.right)

            # Add the number of coins moved through this node
            self.moves += abs(left) + abs(right)

            # Return the net number of coins to pass to the parent
            # node.val - 1 is the excess/deficit at this node after keeping 1 coin
            return left + right + node.val - 1

        helper(root)
        return self.moves