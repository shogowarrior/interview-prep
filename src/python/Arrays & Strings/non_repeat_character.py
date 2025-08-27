# Given: A string of alphanumeric characters with a length between 0 and 1000
# Task: Return the first character in the string that does not repeat


from collections import Counter

def first_non_repeating_character(s: str) -> str:
    char_count = Counter(s)
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return ''  # Return empty string if no non-repeating character is found


print(first_non_repeating_character("abacabad"))  # Output: 'c'