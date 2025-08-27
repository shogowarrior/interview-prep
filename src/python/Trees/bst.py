class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=" ")
                _inorder(node.right)
        _inorder(self.root)

    def height(self, node):
        if node is None:
            return -1  # If the node is None, height is -1 (empty tree case)

        # Recursively find the height of left and right subtrees
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # The height of the current node is the maximum height of its subtrees + 1
        return max(left_height, right_height) + 1
