from bst import BST

# Example usage:
tree = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

print("Inorder traversal:")
tree.inorder()  # Output: 20 30 40 50 60 70 80

# Search for a value
found = tree.search(60)
print("\nFound!" if found else "\nNot found.")
