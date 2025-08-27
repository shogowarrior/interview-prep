# 3. Given: A string of alphanumeric characters with a length between 0 and 1000
# Task: Return the first character in the string that does not repeat

# Find the first non-repeating character in a string
from collections import Counter

def first_non_repeating_char(s: str) -> str:
    # Count the occurrences of each character
    char_count = Counter(s)
    
    # Iterate through the string to find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return ""  # Return an empty string if no non-repeating character is found

# Example usage
if __name__ == "__main__":
    test_strings = ["leetcode", "loveleetcode", "aabbcc"]
    for test in test_strings:
        result = first_non_repeating_char(test)
        print(f"First non-repeating character in '{test}': '{result}'")
# Output:
# First non-repeating character in 'leetcode': 'l'
# First non-repeating character in 'loveleetcode': 'v'
# First non-repeating character in 'aabbcc': ''
# (No non-repeating character)
# Note: The function handles empty strings and strings with all repeating characters by returning an empty string