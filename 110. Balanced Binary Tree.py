"""Given a binary tree, determine if it is height-balanced."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]


    #Print the binary tree in in-order traversal
    def inOrderTraversal(self, Node: TreeNode):
        if (Node == None):
            return
        self.inOrderTraversal(Node.left)
        print(Node.val, end=" ")
        self.inOrderTraversal(Node.right)

#Time Complexity: O(n) , visit every node once only
