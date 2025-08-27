from collections import Counter

def minLengthSubstring(s, t):
    """
    Simpler solution using sliding window with Counter for character frequency.
    """
    if not s or not t:
        return -1

    # Count characters needed in string t
    target_counts = Counter(t)
    required_chars = len(target_counts)
    
    left = 0
    min_length = float('inf')
    current_counts = Counter()
    formed = 0  # Number of unique characters that meet the required frequency

    for right, char in enumerate(s):
        current_counts[char] += 1

        # If current character count matches target count, increment formed
        if char in target_counts and current_counts[char] == target_counts[char]:
            formed += 1

        # Try to shrink the window from the left
        while formed == required_chars and left <= right:
            window_length = right - left + 1
            min_length = min(min_length, window_length)

            # Remove the leftmost character
            left_char = s[left]
            current_counts[left_char] -= 1

            # If we lost a required character, decrement formed
            if left_char in target_counts and current_counts[left_char] < target_counts[left_char]:
                formed -= 1

            left += 1

    return min_length if min_length != float('inf') else -1

# Alternative: Even simpler with Counter subtraction
from collections import Counter

def minLengthSubstring_simple(s, t):
    """
    Ultra-simple solution using Counter subtraction.
    """
    if not s or not t:
        return -1

    target = Counter(t)
    left = 0
    min_len = float('inf')

    print(target)
    
    for right in range(len(s)):
        # Add character to window
        target[s[right]] -= 1
        print("inside", target)
        
        # Check if window is valid (all counts <= 0)
        while all(count <= 0 for count in target.values()) and left <= right:
            min_len = min(min_len, right - left + 1)
            target[s[left]] += 1  # Remove left character
            left += 1
            print(left, right)
            print("inside while", target)
    
    return min_len if min_len != float('inf') else -1

# Test cases
s = "eeeabdcbefebce"
t = "fd"
print("Original:", minLengthSubstring(s, t))  # Output: 5
print("Simple:", minLengthSubstring_simple(s, t))  # Output: 5
