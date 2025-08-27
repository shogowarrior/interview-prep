from bst import BST

tree = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

print(tree.height(tree.root))