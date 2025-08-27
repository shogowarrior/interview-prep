class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_right_leaves(root):

    def dfs(node, is_right):
        
        # Base case: if the node is None, return 0
        if not node: 
            return 0
        # If it's a leaf node and it's a right leaf, return its value
        if not node.left and not node.right and is_right: 
            return node.val
        # Recursively call for left and right children
        return dfs(node.left, False) + dfs(node.right, True) # If it's a right child, pass True

    return dfs(root, False)

# Build the tree: [3, 9, 20, None, None, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(sum_of_right_leaves(root))  # Output: 7


    #   3
    #  / \
    # 9  20
    #    /  \
    #   15   7
