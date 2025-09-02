from utils import assert_custom, print_test_index


def flatten_array(input: list) -> list[int]:

    result = []
    for item in input:
        if type(item) is list:
            result.extend(flatten_array(item))
        else:
            result.append(item)
    return result

test_cases = [
    {"input": [1, [2, 3], [4, [5, 6]], 7], "expected": [1, 2, 3, 4, 5, 6, 7]},
    {"input": [[1, 2], [3, 4], [5, 6]], "expected": [1, 2, 3, 4, 5, 6]},
]

for index in range(len(test_cases)):
    print_test_index(index)
    test_case:map = test_cases[index]
    input: list = test_case["input"]
    expected: list[int] = test_case["expected"]
    observed: list[int] = flatten_array(test_case["input"])
    assert_custom(expected, observed)
    