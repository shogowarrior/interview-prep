from utils import assert_custom, print_test_index


test_cases = [
    {"input": "/home/", "expected": "/home"},
    {"input": "/home//foo/", "expected": "/home/foo"},
    {"input": "/home/user/Documents/../Pictures", "expected": "/home/user/Pictures"},
    {"input": "/../", "expected": "/"},
    {"input": "/.../a/../b/c/../d/./", "expected": "/.../b/d"},
]


def simplify_path(path: str) -> str:
    return None


for index in range(len(test_cases)):
    print_test_index(index)
    test_case = test_cases[index]
    input = test_case["input"]
    expected = test_case["expected"]
    observed = simplify_path(input)
    assert_custom(expected, observed)
