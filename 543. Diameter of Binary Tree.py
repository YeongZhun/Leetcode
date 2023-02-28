"""Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            nonlocal diameter

            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(left + right, diameter)

            return max(left,right) + 1
        
        diameter = 0 
        dfs(root)
        return diameter
    
#Time complexity: O(n) linear