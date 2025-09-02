from utils import assert_custom, print_test_index



class TreeNode:
    
    def __init__(self, value:int=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_bt_from_inorder(inorder_list) -> TreeNode:
    def build_recursive(start, end):
        if start > end:
            return None

        mid = (start + end) // 2  # Find the middle element
        root = TreeNode(inorder_list[mid])  # Make it the root of the current subtree

        root.left = build_recursive(start, mid - 1)  # Recursively build left subtree
        root.right = build_recursive(mid + 1, end)  # Recursively build right subtree

        return root

    if not inorder_list:
        return None

    return build_recursive(0, len(inorder_list) - 1)

def build_bt_from_preorder(values):
    """Build binary tree from preorder list with None for missing children"""
    if not values:
        return None, 0  # return node and index

    root = TreeNode(values[0])
    index = 1

    # If the next value exists and is not None, build left subtree
    if index < len(values) and values[index] is not None:
        root.left, used = build_bt_from_preorder(values[index:])
        index += used
    else:
        root.left = None
        index += 1  # skip None

    # If the next value exists and is not None, build right subtree
    if index < len(values) and values[index] is not None:
        root.right, used = build_bt_from_preorder(values[index:])
        index += used
    else:
        root.right = None
        index += 1  # skip None

    return root, index


def print_bt(node:TreeNode) -> None:
    if not node:
        return
    print_bt(node.left)
    print(node.value)
    print_bt(node.right)

def is_valid_bst(node:TreeNode, min_value, max_value) -> bool:
    if node is None:
        return True
    if not (min_value < node.value < max_value):
        return False
    return is_valid_bst(node.left, min_value, node.value) and is_valid_bst(node.right, node.value, max_value)


test_cases = [
    {
        "input": [2, 1, 3],
        "expected": True
    },
    # {
    #     "input": [5, 1, 4, None, None, 3, 6],
    #     "expected": False
    # }
]



for index in range(len(test_cases)):
    print_test_index(index)
    input:list = test_cases[index]["input"]
    expected:int = test_cases[index]["expected"]

    bt, _ = build_bt_from_preorder(input)
    observed = is_valid_bst(bt, float('-inf'), float('inf'))
    print(observed)
    # assert_custom(observed, expected)
