# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root):
        current = root

        if current is None:
            return None

        temp = current.left
        current.left = current.right
        current.right = temp

        self.invertTree(current.left)
        self.invertTree(current.right)
        print(root)
        return root


root = [4, 2, 7, 1, 3, 6, 9]
