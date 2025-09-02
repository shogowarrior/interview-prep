def print_test_index(index: int):
    print(f"\nTest Case: {index+1}")

def assert_custom(observed, expected):
    print(f"Expected : {expected}")
    print(f"Observed : {observed}")
    assert observed == expected, f"{observed} doesn't match expected {expected}"