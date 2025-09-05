from utils import assert_custom, print_test_index

test_cases = [
    {"input": [1,1,1,2,2,3], "expected": [1,1,2,2,3]},
    {"input": [0,0,1,1,1,1,2,3,3], "expected": [0,0,1,1,2,3,3]},
]


def remove_duplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i

for index in range(len(test_cases)):
    print_test_index(index)
    test_case = test_cases[index]
    input = test_case["input"]
    expected = test_case["expected"]
    observed = remove_duplicates(input)

    assert_custom(len(expected), observed)
    assert_custom(expected, input[:observed])
