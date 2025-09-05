from utils import assert_custom, print_test_index

def three_sum_closest(nums: list, target: int):

    nums.sort()    
    closest_sum = float('inf')

    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            # if current_sum > target + abs(closest_sum-target):
            #     return current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
            
    return closest_sum


test_cases = [
    {"input": {"nums": [-1, 2, 1, -4], "target": 1}, "expected": 2},
    {"input": {"nums": [0, 0, 0], "target": 1}, "expected": 0},
]


for index in range(len(test_cases)):
    print_test_index(index)
    test_case = test_cases[index]
    input = test_case["input"]
    expected = test_case["expected"]
    observed = three_sum_closest(input["nums"], input["target"])
    assert_custom(expected, observed)
