"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
#LCA compare 2 nodes, see their common ancestors, the more further down the tree, the better. If p or q is the root node, then confirm answer is the root node, because not possible to have descendants.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            #Check if p and q is on the right side of the root node
            if p.val > cur.val and q.val > cur.val:
                #if yes then move to right of root node, and repeat while loop
                cur = cur.right
            #Check if p and q is on the left side of the root node
            elif p.val < cur.val and q.val < cur.val:
                #if yes then move to left of root node, and repeat while loop
                cur = cur.left
            #If p and q neither on left or right of current cur node, it would mean that the cur node is the PARENT NODE, and IN BETWEEN p and q, which is definitely the lowest common ancestor
            else:
                return cur.val

    #Print the binary tree in in-order traversal
    def inOrderTraversal(self, Node: TreeNode):
        if (Node == None):
            return
        self.inOrderTraversal(Node.left)
        print(Node.val, end=" ")
        self.inOrderTraversal(Node.right)

test_solution = Solution()
root = TreeNode(6)
p = root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

q = root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print("In-order Traversal of current Binary Search Tree: ")
print(test_solution.inOrderTraversal(root))

print("Lowest Common Ancestor for this current Binary Search Tree: ")
print(test_solution.lowestCommonAncestor(root,p,q))

#Time Complexity: O(log n) , NOT O(n) as we only need to visit at most ONE node in each LEVEL of the Binary Search Tree. So we are looking at the height of the tree, which is log n.
#Space Complexity: O(1) , we did not create any new data.