from collections import Counter
import math


def return_missing_balanced_numbers_2(input):
    counts = Counter(input)
    max_freq = max(counts.values()) if counts else 0
    missing_counts = {k: max_freq - v for k, v in counts.items() if v < max_freq}
    return missing_counts


def return_missing_balanced_numbers_1(input):
    if len(input) == 0:
        return {}

    # count each item and max count
    max_count = 1
    input_count = {}

    for item in input:
        if item in input_count:
            input_count[item] += 1
            if input_count[item] > max_count:
                max_count = input_count[item]
        else:
            input_count[item] = 1

    # remove max count & update input_count
    for key in list(input_count.keys()):
        if input_count[key] == max_count:
            del input_count[key]
        else:
            input_count[key] = max_count - input_count[key]
    return input_count


# This function is a wrapper to call both methods and check if they return the same result
def return_missing_balanced_numbers(input):
    output_1 = return_missing_balanced_numbers_1(input)
    output_2 = return_missing_balanced_numbers_2(input)
    assert output_1 == output_2, "Both methods should return the same result"
    return return_missing_balanced_numbers_1(input)


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(wrongTick, "Test #", test_case_number, ": Expected ", sep="", end="")
        print(expected)
        print(" Your output: ", end="")
        print(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # Testcase 1
    input_1 = ["b", "abc", "c", "a", "a"]
    output_1 = return_missing_balanced_numbers(input_1)
    expected_1 = {"b": 1, "abc": 1, "c": 1}
    check(expected_1, output_1)

    # Testcase 2
    input_2 = [1, 3, 4, 2, 1, 4, 1]
    output_2 = return_missing_balanced_numbers(input_2)
    expected_2 = {2: 2, 3: 2, 4: 1}
    check(expected_2, output_2)

    # Testcase 3
    input_3 = [4, 5, 11, 5, 6, 11]
    output_3 = return_missing_balanced_numbers(input_3)
    expected_3 = {4: 1, 6: 1}
    check(expected_3, output_3)

    # Testcase 4
    input_4 = []
    output_4 = return_missing_balanced_numbers(input_4)
    expected_4 = {}
    check(expected_4, output_4)

    # Testcase 5
    input_5 = [0]
    output_5 = return_missing_balanced_numbers(input_5)
    expected_5 = {}
    check(expected_5, output_5)

    # Testcase 5
    input_6 = [0, 1, 2, 3]
    output_6 = return_missing_balanced_numbers(input_6)
    expected_6 = {}
    check(expected_6, output_6)
