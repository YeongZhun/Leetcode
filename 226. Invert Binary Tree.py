"""Given the root of a binary tree, invert the tree, and return its root."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def invertTree(self, Node: TreeNode) -> TreeNode:
        if (Node == None):
            return 
        else:
            temp = Node

            #Recursively call the function to do left first then right until it hits None (left Node of most left Node in the tree, which will be None)
            self.invertTree(Node.left)
            self.invertTree(Node.right)

            #Swap the left and right Nodes. 
            #If the current Node has no left and right Nodes (the tail end Nodes already), then left and right is just None. None swap with None, is still None. So no change.
            temp = Node.left
            Node.left = Node.right
            Node.right = temp

    #Print the binary tree in in-order traversal
    def inOrderTraversal(self, Node: TreeNode):
        if (Node == None):
            return
        self.inOrderTraversal(Node.left)
        print(Node.val, end=" ")
        self.inOrderTraversal(Node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

test_solution = Solution()
print("In-order Traversal of current binary Tree: ")
print(test_solution.inOrderTraversal(root))

test_solution.invertTree(root)
print("In-order Traversal of inverted binary Tree: ")
print(test_solution.inOrderTraversal(root))

#Time Complexity: O(n) , need to travel to every node
#Space Complexity: O(n) 

class Solution2():
    def invertTree(self, Node: TreeNode) -> TreeNode:
        if (Node == None):
            return 
        else:
            #Recursively call the function 
            root.left, root.right = self.invertTree(root.right), self.invertTree(Node.left)
