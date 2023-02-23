"""Given a binary tree, determine if it is height-balanced."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        return
    #Print the binary tree in in-order traversal
    def inOrderTraversal(self, Node: TreeNode):
        if (Node == None):
            return
        self.inOrderTraversal(Node.left)
        print(Node.val, end=" ")
        self.inOrderTraversal(Node.right)

#Time Complexity: O(n) , visit every node once only